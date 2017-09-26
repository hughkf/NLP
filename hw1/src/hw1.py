# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:18:15 2017

@author: Hugh Krogh-Freeman
"""
import utils
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
import sys
from datetime import datetime

print (datetime.now())
train_filename = sys.argv[1]
test_filename = sys.argv[2]

'''Best Model: Naive Bayes using unigrams'''
utils.classify(train_filename, test_filename)
utils.analyze('model.pkl', 'test.pkl')

'''get data for training and testing'''
train, y_train = utils.get_data(train_filename)
test, y_test = utils.get_data(test_filename)

'''Naive Bayes: unigrams'''
print ('\n\n~~~ Naive Bayes model using unigrams ~~~')
utils.doit(train, y_train, test, y_test, MultinomialNB(alpha=0.2), 1)

'''SVM: bigrams'''
print ('\n\n~~~ Linear SVM model using bigrams ~~~')
svc = LinearSVC(dual=False, penalty='l2', C=1.0, loss='squared_hinge')
utils.doit(train, y_train, test, y_test, svc, 2)

'''logistic regression: trigrams'''
print ('\n\n~~~ Logistic regression model using trigrams ~~~')
# select features
clf = LogisticRegression(solver='newton-cg', max_iter=1000, C=1.0, 
                         fit_intercept=True, penalty='l2')
utils.doit(train, y_train, test, y_test, clf, 3)

print (datetime.now())
