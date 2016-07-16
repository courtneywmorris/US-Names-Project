# What's in a Name?

## Latent naming features in America

### Introduction

The aim of this project is to find subsurface relationships in vectors of names over time in the United States as a means to provide people looking for naming inspiration with new ideas. Doing straight time series analysis on the dataset has already been done, and the goal of this project is to provide an alternative approach to finding name trends. There are two main components of the analysis and resulting model:

1. Normalization of name count data (broken down by state and year) over the past century using TF-IDF vectorization;
2. Pulling latent features from the data using non-negative matrix factorization that can be compared to a user's own naming preferences to provide.

The result of the model will be a list of latent features which are described by a series of names and geographies associated with that latent feature.

### Data

The data for this project comes from US Social Security Administration. There is a [clean Kaggle dataset](https://www.kaggle.com/kaggle/us-baby-names) that of names from 1910-2014. Counts of first names are broken down by US state and year, with a gender specified for each name.

#### Data Preparation

In order to model the name relationships, I formulated a matrix for each male and female names. This allows for the analysis to focus on the latent features associated with preferences for each gender. (Interesting point: there are about 2X as many unique female names compared to male names.) The resulting matrix was in this format:

![alt text](images/matrix.png)

### Normalization - Vectorization

I normalized the data in order to limit the influence of highly popular names over time and states with large populations. I found that TF-IDF vectorization was effective for this normalization, and it appears to be a new approach to analyzing name data. Just like using TF_IDF down-weights the importance of the word “the” and longer documents in NLP, it has done the same here.

This allowed for medium-popular names and smaller states to also show up in latent feature descriptions. In effect, the model produces a more diverse set of latent features, which allows for a nuanced set of names suggestions to surface (think sub-genres like Bill Murray films or British comedy recommendations in movie terms).

### Matrix Factorization

To extract latent features from this matrix, I applied non-negative matrix factorization. NMF produces two matrices, one which connects the relationship between latent features and year-state, the other which connects first names to latent features.

NMF is better for this analysis than PCA dimensionality reduction or SVD matrix factorization, because keeping the values of the factored matrices positive lines up with our intuitive understanding of name popularity (which are all based in positive values).

NMF also enables us to distill the data down to parts-specific latent features, in this case latent features associated with a specific group of names or a specific state and time period—compared with making generalizations about important features for the entire US as a whole for the entire past century at once.

### Application

Let’s say I’m a to-be parent who is interested in naming my daughter something akin to my favorite Game of Thrones characters. I create a vector of names with my “votes” for each name, and run it through the model. Here the larger the name, the stronger my preference for that name.

![alt text](images/input_vector.png)

After transforming the vector through the model, we can rank which latent features are weighted strongest and produce a list of the year-states and names which best describe those latent features. There is now a list of new names with a geographic-timestamp to add some flavor to my naming research.

**Names**
![alt text](images/output_vector.png)

**Geography-Time Period**
![alt text](images/latent_feature2.png)
