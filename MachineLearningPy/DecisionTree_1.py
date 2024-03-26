import pandas as pd

df=pd.read_csv('titanic.csv')
inputs= df.drop(['Survived','PassengerId','Name','SibSp','Ticket','Cabin','Embarked','Survived','Parch'],axis='columns')

target = df['Survived']
# print(inputs)
# print(target)
from sklearn.preprocessing import LabelEncoder as le
le_Sex =  le()

inputs['Sex_n']=le_Sex.fit_transform(inputs['Sex'])

# print(inputs)
inputs_n = inputs.drop('Sex',axis='columns')
print(inputs_n)
print(inputs_n.corr())

from sklearn import tree as t

model= t.DecisionTreeClassifier()
model.fit(inputs_n,target)
print("Score of our model is:",model.score(inputs_n,target))

print(model.predict([[3,22,54.87,1]]))
