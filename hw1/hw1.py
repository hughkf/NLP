# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:18:15 2017


@author: Hugh Krogh-Freeman
"""
import utils
from analyze import analyze
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import sys
from sklearn.metrics import confusion_matrix
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from datetime import datetime

print (datetime.now())
train_filename = sys.argv[1]
test_filename = sys.argv[2]

'''Best Model: Naive Bayes using unigrams''' # 0.6236 -> 0.6244 -> 0.6252
utils.classify(train_filename, test_filename)
analyze('model.pkl', 'test.pkl')

'''get data for training and testing'''
train, y_train = utils.get_data(train_filename)
test, y_test = utils.get_data(test_filename)

'''SVM: bigrams'''
print ('\n\n~~~ Linear SVM model using bigrams ~~~')
# select features
X_train, X_test, vectorizer = utils.get_features(train, y_train, test, ngram=2)
sel = SelectKBest(mutual_info_classif, k=300)
sel.fit(X_train, y_train)
# train and test
clf = LinearSVC(dual=False, penalty='l2', C=1.0, loss='squared_hinge')
clf.fit(X_train.tocsr()[:,sel.get_support()], y_train)
print ('* Accuracy:', clf.score(X_test.tocsr()[:,sel.get_support()], y_test))
print ('* Top 20 features:')
print (utils.print_top20_features(clf, 
                      utils.get_feature_names(vectorizer)[sel.get_support()]))
print ('* Continency matrix:')
y_pred = clf.predict(X_test.tocsr()[:,sel.get_support()])
print (confusion_matrix(y_test, y_pred))

'''logistic regression: trigrams'''
print ('\n\n~~~ Logistic regression model using trigrams ~~~')
# select features
X_train, X_test, vectorizer = utils.get_features(train, y_train, test, ngram=3)
sel = SelectKBest(mutual_info_classif, k=300)
sel.fit(X_train, y_train)
# train and test
clf = LogisticRegression(solver='newton-cg', max_iter=1000, C=1.0, 
     fit_intercept=True, penalty='l2')
clf.fit(X_train.tocsr()[:,sel.get_support()], y_train)
print ('* Accuracy:', clf.score(X_test.tocsr()[:,sel.get_support()], y_test))
print ('* Top 20 features:')
print (utils.print_top20_features(clf, 
                      utils.get_feature_names(vectorizer)[sel.get_support()]))
print ('* Continency matrix:')
y_pred = clf.predict(X_test.tocsr()[:,sel.get_support()])
print (confusion_matrix(y_test, y_pred))
print (datetime.now())
