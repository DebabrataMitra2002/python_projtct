import pandas as pd 
from sklearn.datasets import load_iris 
iris=load_iris()
print(dir(iris))
# print(iris.feature_names)
df=pd.DataFrame(iris.data,columns=iris.feature_names)
# print(df.head(10))
 rint(iris.target_names)
df['target']= iris.target
df['flower_name'] =df.target.apply(lambda x: iris.target_names[x])
# print(df.head())

X= df.drop(['target','flower_name'], axis='columns')

y = df.target
# print(y)
df0 = df[:50]
df1 = df[50:100]
df2 = df[100:]
import matplotlib.pyplot as plt
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'],color="green",marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'],color="blue",marker='.')
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'],color="red",marker='*')
plt.show()
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'],color="green",marker='+')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'],color="blue",marker='.')
plt.scatter(df2['petal length (cm)'], df2['petal width (cm)'],color="red",marker='*')
plt.show()
from sklearn.model_selection import train_test_split 
x_train , x_test,y_train,y_test = train_test_split(X,y,test_size=0.20)

from sklearn.svm import SVC
model = SVC()
model.fit(x_train, y_train)
y_pred=model.predict(x_test)

from sklearn.metrics import confusion_matrix as cm
print("confusion matrix of y_pred vs y_test:\n",cm(y_pred,y_test))
print(model.score(x_test,y_test))
