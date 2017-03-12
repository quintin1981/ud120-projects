# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:16:10 2017

@author: Computer
"""

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

word_data = pickle.load(open("your_word_data.pkl", "r"))
email_authors = pickle.load(open("your_email_authors.pkl", "r"))

vectorizer = TfidfVectorizer(stop_words='english')

features_train_transformed = vectorizer.fit_transform(word_data)

test = vectorizer.get_feature_names()

print test[34597]