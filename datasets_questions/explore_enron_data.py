#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

array = enron_data.keys()

count = 0

num_poi = 0

while count < len(array):
    if enron_data[array[count]]['poi'] == True:
        num_poi = num_poi + 1
        count = count + 1
    else:
        count = count + 1
        
print ("Number POI's: ", num_poi)
        
#key = array[2]

#print enron_data[key]['poi']

 