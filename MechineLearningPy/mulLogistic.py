from sklearn.datasets import load_iris
# load data in iris from load:
iris= load_iris()
# print(dir(iris));


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.20)

from sklearn.linear_model import LogisticRegression as Lg
model=Lg() # create a object of class Lg:
model.fit(x_train,y_train)

# print(model.predict(iris.data[0:10]))
y_pre=model.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_pre,y_test)
print(cm)
print(model.score(x_test,y_test))

import matplotlib.pyplot as plt
import seaborn as sb
plt.figure(figsize = (10,7))
sb.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()


