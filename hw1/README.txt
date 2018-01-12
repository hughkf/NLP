* Name: Hugh Krogh-Freeman
* Email: hk2903@columbia.edu
* Homework: #1

* How to train and test classifier: 
~ Run "classify.py [train filename] [test filename]"
	e.g. classify.py ./train.txt ./test.txt
or 
~ Run "hw1.py [train filename] [test filename]"
	e.g. hw1.py ./train.txt ./test.txt

* Special features and limitations of this classifier:
~ There are only two classes: 1 for Democrat, 0 for Republican
~ The input must have each example on a separate line with the class label at the end of the line, i.e. either "democrat" for class 1 or anything else for class 0.
~ This classifier ignores syntax
~ This classifier requires an external library: "emoji"
~ This classifier has additional methods inherited from the Sci-kit Learn library:
- predict_proba(): Return probability estimates for the test vector X.
- predict_log_proba(): Return log-probability estimates for the test vector X.
- partial_fit(X, y[, classes, sample_weight]): Incremental fit on a batch of samples.
- get_params([deep]): Get parameters for this estimator.
- score(X, y[, sample_weight]): Returns the mean accuracy on the given test data and labels.
- predict(X): Perform classification on an array of test vectors X.
~ The code pickles data in order to pass it around and for the purpose of precomputation. 
- Classify(), pickles the feature names of the best-scoring model, which are used later by analyze() to print the top 20 features: "feature_names.pkl".
- Classify() also pickles the vectorized test data used by analyze() to print the confusion matrix: "test.pkl".
- We have pickled the features pre-selected for each of the other, three models which are trained and scored in doit() in hw1.py: ngram=1_feature_indices.pkl, ngram=2_feature_indices.pkl, and ngram=3_feature_indices.pkl.