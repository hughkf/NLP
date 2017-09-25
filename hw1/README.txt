* Name: Hugh Krogh-Freeman
* Email: hk2903@columbia.edu
* Homework: #1
* How to train and test classifier: 
- Run "classify.py [train filename] [test filename]"
- e.g. classify.py ./train.txt ./test.txt

* Special features and limitations of this classifier:
- There are only two classes: 1 for Democrat, 0 for Republican
- The input must have each example on a separate line with the class label at the end of the line, i.e. either "democrat" for class 1 or anything else for class 0.
- This classifier ignores syntax
- This classifier requires an external library: "emoji"
- This classifier has additional methods inherited from the Sci-kit Learn library:
> predict_proba(): Return probability estimates for the test vector X.
> predict_log_proba(): Return log-probability estimates for the test vector X.
> partial_fit(X, y[, classes, sample_weight]): Incremental fit on a batch of samples.
> get_params([deep]): Get parameters for this estimator.
> score(X, y[, sample_weight]): Returns the mean accuracy on the given test data and labels.
> predict(X): Perform classification on an array of test vectors X.