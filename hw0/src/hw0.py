'''
Name: Hugh Krogh-Freeman
UNI: hk2903
Date: 2017-09-10
Class: COMS W4705.001
'''
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.metrics
import sklearn.neighbors
import matplotlib.pyplot as plt
import numpy as np

print("Loading 20 newsgroups dataset for categories:")
data_train = fetch_20newsgroups(subset='train', shuffle=True, random_state=42)
data_test = fetch_20newsgroups(subset='test', shuffle=True, random_state=42)
print('data loaded')

'''Create tf-idf vectors for the input'''
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.9,
                                 stop_words='english')
X_train = vectorizer.fit_transform(data_train.data)
X_test = vectorizer.transform(data_test.data)
y_train = data_train.target
y_test = data_test.target

'''Prepare data to plot'''
f1_scores = []
ks = []

# loop through each k between 2 and 50
# train and test KNN model
for n_neighbors in range(2, 51):
    
    '''Train a K-Neighbors Classifier on the data'''
    weights = 'uniform'
    clf = sklearn.neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X_train, y_train)

    '''Make predictions on the test data using the trained classifier'''
    y_predicted = clf.predict(X_test)

    f1_scores.append(sklearn.metrics.f1_score(y_true=y_test, 
                                              y_pred=y_predicted, average='weighted'))
    ks.append(n_neighbors)

plt.plot(ks, f1_scores, c='r') # red
plt.title('F1 score by number of nearest neighbors') # title
plt.xlabel('Nearest neighbors') # x-axis
plt.ylabel('F1 score') # y-axis
plt.xticks(np.arange(min(ks), max(ks)+1, 2.0)) # even tick marks
plt.show() # k=40 gives better or the same results as k=50
