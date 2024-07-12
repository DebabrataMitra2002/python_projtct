import os
import pickle

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree

base_path = os.getcwd()
pickle_path = os.path.normpath(base_path + os.sep + 'pickle')


class TwoPeopleActivity:
    # train model
    def __init__(self):
        # check if model exists, then do nothing, else train model
        try:
            pickle_file = os.path.normpath(pickle_path + os.sep + 'model.sav')
            self.model = pickle.load(open(pickle_file, 'rb'))
        except:
            self.train()

    def train(self):
        training_data = os.path.normpath(pickle_path + os.sep + 'updated_tulum.csv')
        df = pd.read_csv(training_data)
        df = df.replace(np.nan, 0)
        feature = df.iloc[:, 2:22]
        labels = df.loc[:, 'R1_Annotation':'R2_Annotation']
        train, test, train_labels, test_labels = train_test_split(feature, labels, test_size=0.1, random_state=4)
        gnb = tree.DecisionTreeClassifier()
        model = gnb.fit(train, train_labels)

        pickle_file = os.path.normpath(pickle_path + os.sep + 'model.sav')
        pickle.dump(model, open(pickle_file, 'wb'))
        self.model = model

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction

#
# Two = TwoPeopleActivity()
# Two.train()
# data = np.array([[
#     0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
#
#     0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
#
# print(Two.predict(data))
