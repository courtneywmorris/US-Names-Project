import pandas as pd

def clean_data(df):
    df['new_name'] = df.Name.str.lower()
    df = df.set_index(['Year','State'])
    df['name_gender'] = zip(df.new_name, df.Gender)
    df = df.drop(['Year', 'State', 'new_name', 'Id', 'Name'])

    date_state_series = df.groupby(df.index).sum()['Count']
    df['tuple_index'] = df.index.values
    df = df.join(date_state_series, how='left', on='tuple_index', lsuffix='_by_name')

    df['count_norm'] = df.Count_by_name / df.Count

    return df

def time_period_clean(df, start_date, end_date):
    df = df[(df['Year'] >= start_date) & (df['Year'] <= end_date)]
    df['new_name'] = df.Name.str.lower()
    df = df.set_index(['Year','State'])
    df['name_gender'] = zip(df.new_name, df.Gender)
    df = df.drop(['Year', 'State', 'new_name'])

    date_state_series = df.groupby(df.index).sum()['Count']
    df['tuple_index'] = df.index.values
    df = df.join(date_state_series, how='left', on='tuple_index', lsuffix='_by_name')

    df['count_norm'] = df.Count_by_name / df.Count

    return df

def pivot_data(df, pivot_vals, pivot_index, pivot_cols):
    data_pivot = pd.pivot_table(df, values=pivot_vals, index=pivot_index, columns=pivot_cols)
    data_pivot = data_pivot.fillna(0)
    return data_pivot
