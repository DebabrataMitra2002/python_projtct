# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:40:31 2018

@author: USER
"""

import pandas as pd
import numpy as np
import os
from sklearn import svm 
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

cwd = os.getcwd()
cwd
#data_set = pd.read_csv("Day 1 to 5_new.csv")
#data_set = pd.read_csv("day1_5manually_annotated_nt_only5.csv") 
#data_set = pd.read_csv("day1_5manually_annotated_nt.csv")
data_set=pd.read_csv("newest_aruba.csv")
data_set=data_set.replace(np.nan,0)
data_set.head()
#type(data_set)
#data_set['annotation']
#annotation_mapping = {'bed_to_toilet':1,'slepping':2,'Meal_preparation':3,'Relax':4,'Eating':5,'Wash_dishes':6,'Work':7,'Other':8}
#data_set['annotation']= data_set['annotation'].map(annotation_mapping)
#print(data_set['annotation'])
labels = data_set['Annotation']
print("The labels are", labels)

feature = data_set.iloc[:,2:38]
feature

train, test, train_labels, test_labels = train_test_split(feature,labels,test_size=0.5,random_state=4)
print(train)
gnb = tree.DecisionTreeClassifier()
model = gnb.fit(train, train_labels)
print("model",model)
preds = gnb.predict(test)
print(preds)
print(test_labels)
print(accuracy_score(test_labels, preds))
