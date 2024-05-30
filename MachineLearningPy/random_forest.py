from matplotlib import pyplot as plt
import pandas as pd
from  sklearn.datasets import load_digits
digits = load_digits()
# print(dir(digits))
df = pd.DataFrame(digits.data)

# print(df.head())

df['target'] = digits.target

x= df.drop('target',axis='columns')
y = df.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
model.fit(x_train ,y_train)

print(model.score(x_test,y_test))
y_predicted = model.predict(x_test)
from sklearn.metrics import confusion_matrix as cM
cm = cM(y_test,y_predicted)
print(cm)
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm,annot=True)
plt.xlabel=('pridected value')
plt.ylabel=('real value')
plt.show()

