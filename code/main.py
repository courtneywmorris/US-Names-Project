import pandas as pd
from preprocessing import InputFrame
from tf_idf import TfIdf
from NMF import LatentFeatures
import cPickle as pk

filename = '../../StateNames.csv'
dataframe = pd.read_csv(filename)

#Run the male preprocessing and model
male_instance = InputFrame(dataframe,'M')
male_instance.clean_data_from_frame()
male_frame = male_instance.gender_frame

male_tfidf = TfIdf(male_frame)
male_vectors = male_tfidf.tfidf_matrix()

male_nmf = LatentFeatures(male_vectors)
male_matrices = male_nmf.fit_model()

# male_nmf.print_W_H_features(male_tfidf.index, male_tfidf.features, 20)
male_features_dict = male_nmf.latent_features_dict(male_tfidf.index, male_tfidf.features, 20)

#Store the male model and latent features dictionary
with open('../data/male_nmf.pkl','w') as f:
    pk.dump(male_nmf,f)

with open('../data/male_latent_features.pkl','w') as f:
    pk.dump(male_features_dict,f)



#Run the female preprocessing and model
female_instance = InputFrame(dataframe,'F')
female_instance.clean_data_from_frame()
female_frame = female_instance.gender_frame

female_tfidf = TfIdf(female_frame)
female_vectors = female_tfidf.tfidf_matrix()

female_nmf = LatentFeatures(female_vectors)
female_matrices = female_nmf.fit_model()

# female_nmf.print_W_H_features(female_tfidf.index, female_tfidf.features, 20)
female_features_dict = female_nmf.latent_features_dict(female_tfidf.index, female_tfidf.features, 20)

#Store the female model and latent features dictionary
with open('../data/female_nmf.pkl','w') as f:
    pk.dump(female_nmf,f)

with open('../data/female_latent_features.pkl','w') as f:
    pk.dump(female_features_dict,f)
