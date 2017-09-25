# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:40:16 2017

@author: Hugh Krogh-Freeman
"""
from sklearn.feature_selection import SelectKBest, mutual_info_classif
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import hstack
import emoji
from sklearn.naive_bayes import MultinomialNB
import pickle
from sklearn.metrics import confusion_matrix

def get_char_count(text_list):
    '''Tweet character count'''
    return np.array([len(x) for x in text_list], ndmin=2).T

def get_word_count(text_list):
    '''Tweet count of words'''
    return np.array([len(x.split()) for x in text_list], ndmin=2).T

def get_emoji_feature(text_list):
    '''emoji presence feature'''
    def count_emoji(input_string):
        '''utility function for counting emoji'''
        cnt = 0
        for character in input_string:
            if character.encode('ascii', 'ignore').decode('ascii') == '':
                cnt += 1
        return cnt
    return np.array([count_emoji(x) for x in text_list], ndmin=2).T

def get_exclamation_feature(text_list):
    '''double exclamation feature''' 
    return np.array([x.count("!") for x in text_list], ndmin=2).T

def get_question_feature(text_list):
    '''double question feature''' 
    return np.array([x.count("?") for x in text_list], ndmin=2).T

def get_all_caps_feature(text_list):
    '''All caps feature'''
    return np.array([len([y for y in x.split() if y == y.upper()]) for x in 
                     text_list], ndmin=2).T

def get_republican_vocabulary(republican_text_list, max_features_ratio=1.0):
    '''republican vocabulary'''
    vectorizer = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\S+\b', 
                                 min_df=1, stop_words='english')
    vectorizer.fit(republican_text_list)
    vectorizer = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\S+\b', 
         max_features=int(len(vectorizer.vocabulary_)* max_features_ratio), 
         stop_words='english')
    vectorizer.fit(republican_text_list)
    return vectorizer.vocabulary_

def get_democrat_vocabulary(democrat_text_list, max_features_ratio=1.0):
    '''democrat vocabulary'''
    vectorizer = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\S+\b', 
                                 min_df=1, stop_words='english')
    vectorizer.fit(democrat_text_list)
    vectorizer = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\S+\b', 
         max_features=int(len(vectorizer.vocabulary_)* max_features_ratio), 
         stop_words='english')
    vectorizer.fit(democrat_text_list)
    return vectorizer.vocabulary_

def get_republican_vocabulary_feature(republican_vocabulary, text_list):
    '''republican vocabulary'''
    f = lambda republican_vocabulary, text_string: len([w in 
            republican_vocabulary for w in text_string.split()])
    return np.array([f(republican_vocabulary, x_str) for x_str in text_list], 
                     ndmin=2).T

def get_democrat_vocabulary_feature(democrat_vocabulary, text_list):
    '''democrat vocabulary'''
    f = lambda democrat_vocabulary, text_string: len([w in 
              democrat_vocabulary for w in text_string.split()])
    return np.array([f(democrat_vocabulary, x_str) for x_str in text_list], 
                     ndmin=2).T
    
def get_vocabulary_feature(democrat_vocabulary, republican_vocabulary, text_list):
    '''vocabulary feature'''
    democrat_specific_vocab = set(democrat_vocabulary).difference(
            set(republican_vocabulary))
    f = lambda democrat_specific_vocab, text_string: 0 < len([w in 
                  democrat_specific_vocab for w in text_string.split()])
    return np.array([1 if f(democrat_specific_vocab, x_str) else 0 
                     for x_str in text_list], ndmin=2).T
    
def get_data(filename):
    '''training set preparation'''
    data = []
    y = []
    with open(filename, 'r', encoding='utf8') as f:
        contents = f.read()
        for line in contents.split('\n'):
            pieces = line.split()
            data.append(' '.join(pieces[:-1]))
            y.append(1 if pieces[-1] == 'democrat' else 0)
    return ([ emoji.demojize(x) for x in data ], y)

def get_features(train, y_train, test, ngram=1):
    '''get the feature set for all models'''
    
    '''get republican, democrat vocabularies'''
    republican_tweets = np.array(train)[np.where( np.array(y_train)==0 )]
    democrat_tweets = np.array(train)[np.where( np.array(y_train)==1 )]
    republican_vocabulary = get_republican_vocabulary(republican_tweets)
    democrat_vocabulary = get_democrat_vocabulary(democrat_tweets)
    
    '''unigrams'''
    vectorizer = CountVectorizer(ngram_range=(ngram, ngram), 
         token_pattern=r'\b\S+\b', min_df=1, stop_words='english')
    vectorizer.fit(train)
    X_train_tfmd = hstack((get_exclamation_feature(train), 
                          get_all_caps_feature(train), 
                          get_question_feature(train), 
                          get_emoji_feature(train), 
                          get_char_count(train), 
                          get_word_count(train), 
                          get_republican_vocabulary_feature(republican_vocabulary, 
                                                            train),
                          get_democrat_vocabulary_feature(democrat_vocabulary, 
                                                          train),
                          get_vocabulary_feature(democrat_vocabulary, 
                                                 republican_vocabulary, train),
                          vectorizer.transform(train)))
                          
    X_test_tfmd = hstack((get_exclamation_feature(test), 
                        get_all_caps_feature(test), 
                        get_question_feature(test), 
                        get_emoji_feature(test), 
                        get_char_count(test), 
                        get_word_count(test), 
                        get_republican_vocabulary_feature(republican_vocabulary, 
                                                          test),
                        get_democrat_vocabulary_feature(democrat_vocabulary, test),
                        get_vocabulary_feature(democrat_vocabulary, 
                                               republican_vocabulary, test),
                        vectorizer.transform(test)))
    return (X_train_tfmd, X_test_tfmd, vectorizer)

def get_feature_names(vectorizer):
    return np.append(np.array(['exclamation_feature', 'all_caps_feature', 
      'question_feature', 'emoji_feature', 'char_count_feature', 
      'word_count_feature', 'republican_vocabulary_feature', 
      'democrat_vocabulary_feature', 'vocabulary_feature']), 
      vectorizer.get_feature_names())

def classify(train_filename, test_filename):
    '''train and test the model with the best parameters'''
    train, y_train = get_data(train_filename)
    test, y_test = get_data(test_filename)
    X_train, X_test, vectorizer = get_features(train, y_train, test)
    
    '''train model'''
    nb = MultinomialNB(alpha=0.2)
    nb.fit(X_train, y_train)
    print ('~~~ Best model ~~~')
    print ('* Accuracy:', nb.score(X_test, y_test))
    with open('model.pkl', 'wb') as f:
        pickle.dump(nb, f)
    
    with open('test.pkl', 'wb') as f:
        pickle.dump([X_test, y_test], f)

    feature_names = get_feature_names(vectorizer)
    with open('features.pkl', 'wb') as f:
        pickle.dump(feature_names, f)

    return X_test, y_test

def print_top20_features(model, feature_names):
    '''sort, index, and print top 20 features'''    
    l = sorted(zip(model.coef_[0], feature_names), reverse=True)    
    return '\n'.join(['%d. feature: "%s" (score: %f)' % (n+1, x[1], x[0]) 
        for n, x in enumerate(l[:20])])

def doit(train, y_train, test, y_test, clf, ngrams):
    '''takes care of training, testing, and printing details about
    each model in hw1.py
    '''
    # select features
    X_train, X_test, vectorizer = get_features(train, y_train, test, ngrams)
    sel = SelectKBest(mutual_info_classif, k=300)
    sel.fit(X_train, y_train)
    # train and test
    clf.fit(X_train.tocsr()[:,sel.get_support()], y_train)
    print ('* Accuracy:', clf.score(X_test.tocsr()[:,sel.get_support()], y_test))
    print ('* Top 20 features:')
    print (print_top20_features(clf, 
                      get_feature_names(vectorizer)[sel.get_support()]))
    print ('* Continency matrix:')
    y_pred = clf.predict(X_test.tocsr()[:,sel.get_support()])
    print (confusion_matrix(y_test, y_pred))