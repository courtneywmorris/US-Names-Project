import pandas as pd
import numpy as np
from clean_data import clean_data_from_frame

def tf_idf_matrix(df, gender):
    df = clean_data_from_frame(df)
    gender_frame = df[df['Gender']==gender]

    pivot = pd.pivot_table(gender_frame, values = 'Count_by_name',
    index = gender_frame.tuple_index, columns= gender_frame.Name)

    doc_freq = pivot.count()
    max_values = pivot.max(axis=1)

    clean_pivot = pivot.fillna(0)
    clean_pivot = (.5 + .5*(clean_pivot.T/max_values)).T

    tf_idf_frame = my_tfidf(clean_pivot, pivot.shape[0],doc_freq)

    return tf_idf_frame

def my_tfidf(df, n_documents, doc_freq_series):
    column_idf = np.log((n_documents + 1.0) / (doc_freq_series + 1.0)) + 1.0
    return df * column_idf

def sklearn_tfidf(df,n_documents, doc_freq_series):
    column_idf = np.log(float(n_documents) / doc_freq_series) + 1.0
    return df * column_idf
