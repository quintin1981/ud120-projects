#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


from sklearn.svm import SVC
clf = SVC(kernel="linear")
t0 = time()
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
clf.fit(features_train, labels_train)

print "training time:", round(time()-t0, 3), "s"

pred = clf.predict(features_test)


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
from sklearn.metrics import accuracy_score
print "Accuracy: ", accuracy_score(pred, labels_test)
#########################################################
### your code goes here ###


#########################################################


