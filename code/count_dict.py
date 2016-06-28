from collections import defaultdict

def vocab(df):
    dictionary = df.to_dict(orient='index')
    all_names = set()

    for k in dictionary:
        all_names.add(k[0])
    return all_names


def counts_dict(df, name_list):
    dictionary = df.to_dict(orient='index')
    names_vals = defaultdict(int)

    for k in dictionary:
        names_vals[k[0]] += dictionary[k]['Count']
    return names_vals


def name_counter(values_dict, name_list):
    output_dict = defaultdict(int)
    for k in values_dict:
        row_name = k[0]
        year = k[1]
        if row_name in name_list:
            output_dict[year] += values_dict[k]['Count']
    return output_dict
