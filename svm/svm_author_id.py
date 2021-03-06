#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
clf = SVC(kernel="rbf", C=10000.0)
t0 = time()
###features_train = features_train[:len(features_train)/100] 
###labels_train = labels_train[:len(labels_train)/100] 
clf.fit(features_train, labels_train)

print "training time:", round(time()-t0, 3), "s"

pred = clf.predict(features_test)

count = len(pred)

i = 0

chris = 0

while i < count:
    if pred[i] == 1:
        chris = chris + 1
        i = i + 1
    else:
        i = i + 1

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
from sklearn.metrics import accuracy_score
print "Accuracy: ", accuracy_score(pred, labels_test)
print("pred[10]: ",pred[10])
print("pred[26]: ",pred[26])
print("pred[50]: ",pred[50])
print("chris: ", chris)
#########################################################
### your code goes here ###


#########################################################






