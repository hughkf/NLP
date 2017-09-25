# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:00:05 2017

@author: Hugh Krogh-Freeman
"""
from sklearn.metrics import confusion_matrix
import pickle
import utils

def analyze(model_filename, vectorized_test_data_filename):

    with open(vectorized_test_data_filename, 'rb') as f:
        vectorized_test_data = pickle.load(f)
        vectorized_test_data_X, vectorized_test_data_y = vectorized_test_data

    with open(model_filename, 'rb') as f:
        model = pickle.load(f)

    '''sort, index, and print top 20 features'''            
    with open('features.pkl', 'rb') as f:
        feature_names = pickle.load(f)
    print ('* Top 20 features:')
    print (utils.print_top20_features(model, feature_names))
    
    '''print confusion matrix'''
    print ('* Continency matrix:')
    y_pred = model.predict(vectorized_test_data_X)
    print (confusion_matrix(vectorized_test_data_y, y_pred))

