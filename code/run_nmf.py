from sklearn.decomposition import NMF
import pandas as pd
import numpy as np

def run_nmf(df,params):
    nmf = NMF(n_components=params)
    W = nmf.fit_transform(df)
    H = nmf.components_
    return W, H, nmf

def recon_error(df, k):
    nmf = NMF(n_components=k)
    W = nmf.fit_transform(df)
    H = nmf.components_
    return nmf.reconstruction_err_

def reconst_error_sum(target, left, right):
    return (np.array(target - left.dot(right))**2).sum()

def print_top_features(W, H, features, top_features, data_matrix):
    print "Reconstruction Error: %f" %reconst_mse(data_matrix, W, H)
    for latent_num, latent in enumerate(H):
        print "Latent Feature %d" % (int(latent_num) + 1)
        print [features[i] for i in latent.argsort()[:-top_features-1:-1]]
        print

def print_year_diff_features(W, H, features, top_features, data_matrix):
    print "Reconstruction Error: %f" %reconst_mse(data_matrix, W, H)
    for latent_num, latent in enumerate(H):
        print "Latent Feature %d" % (int(latent_num) + 1)
        results = [features[i] for i in latent.argsort()[:-top_features-1:-1]]
        result_years = [features[i][0] for i in latent.argsort()[:-top_features-1:-1]]
        year_diff = max(result_years) - min(result_years)
        if year_diff > 10:
            print results

def run_decade_nmf(df, (start_date, end_date), n_factors):
    decade_df = time_period_clean(df, start_date, end_date)
    decade_pivot = pivot_data(decade_df, 'count_norm', 'name_gender', 'tuple_index')

    W, H, nmf = run_nmf(decade_pivot,n_factors)

    state_features = decade_pivot.columns

    print print_top_features(W,H,state_features,15,decade_pivot)

    return W, H, nmf

def run_pop_nmf(df, n_factors):

    W, H, nmf, error = run_nmf(df,n_factors)

    state_features = df.columns

    print "SKlearn error: %f" %error
    print print_year_diff_features(W,H,state_features,20,df)

    return W, H, nmf

def run_tfidf_nmf(array, n_factors, features):

    W, H, nmf, error = run_nmf(df,n_factors)

    print "SKlearn error: %f" %error
    print print_top_features(W,H,features,20,array)

    return W, H, nmf
