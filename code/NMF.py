import numpy as np
import pandas as pd
from sklearn.decomposition import NMF

class LatentFeatures(object):
    '''
    Class to store the NMF object.
    Input: vectorized name dataframe
    Output: NMF sklearn object (including matrices)
    '''
    def __init__(self, data):
        self.data = data
        self.W_matrix = None
        self.H_matrix = None
        self.recon_error = None
        self.model = NMF(n_components=50)
        # self.W_index = data.columns
        # self.H_features = data.index.values

    def fit_model(self):
        '''
        Fits the model and updates values for decomposed matrices.
        '''
        self.W_matrix = self.model.fit_transform(self.data)
        self.H_matrix = self.model.components_
        self.recon_error = self.model.reconstruction_err_

    def reconst_error_sum(self):
        '''
        Calculates reconstruction error of reconstructing original matrix
        using only the W and H (lower dimension) matrices.
        Input: Original matrix, W matrix, H matrix
        Ouput: Total reconstruction error
        '''
        return (np.array(self.data - self.W_matrix.dot(self.H_matrix))**2).sum()

    def print_W_H_features(self, W_features, H_features, n_features):
        for latent_num, latent in enumerate(self.H_matrix):
            print "Latent Feature %d" % (int(latent_num) + 1)
            print [H_features[i] for i in latent.argsort()[:-n_features-1:-1]]
            W_latent = self.W_matrix[:,latent_num]
            print [W_features[i] for i in W_latent.argsort()[:-n_features-1:-1]]
            print

    def latent_features_dict(self, W_features, H_features, n_features):
        master_dict = {}

        for latent_num, latent in enumerate(self.H_matrix):
            master_key = (int(latent_num) + 1)
            feature_dict = {}

            top_h_features = [H_features[i] for i in latent.argsort()[:-n_features-1:-1]]
            W_latent = self.W_matrix[:,latent_num]
            top_w_features = [W_features[i] for i in W_latent.argsort()[:-n_features-1:-1]]

            feature_dict['H'] = top_h_features
            feature_dict['W'] = top_w_features
            master_dict[master_key] = feature_dict

        return master_dict

    def transform_new_vector(self):
        pass
