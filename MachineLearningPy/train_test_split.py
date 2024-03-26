import pandas as pd
from sklearn.model_selection import  train_test_split as tt
from sklearn.linear_model import LinearRegression 

df = pd.read_csv("carprices.csv")
print(df)

""" The approach we are going to use here is to split available data in two sets

1: Training: We will train our model on this dataset
2: Testing: We will use this subset to make actual predictions using trained model
The reason we don't use same training set for testing is because our model has seen those samples before, using same samples for making predictions might give us wrong impression about accuracy of our model. It is like you ask same questions in exam paper as you tought the students in the class. """
x = df[['Mileage','Age(yrs)']]
y = df['Sell Price($)']

x_train,x_test,y_train,y_test = tt(x,y,test_size=0.3)
# create a linear regerraton class object:
reg = LinearRegression()
reg.fit(x_train,y_train)
print(reg.predict(x_test))
print(reg.score(x_test,y_test))
