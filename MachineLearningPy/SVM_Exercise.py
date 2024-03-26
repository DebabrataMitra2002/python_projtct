from string import digits
from sklearn.datasets import load_digits
import pandas as pd

digits =load_digits()
# print(dir(digits))
# print(digits.target_names)
# print(digits.target)
df = pd.DataFrame(digits.data,digits.target)
# print(df)
df['target']=digits.target
# print(df['target'])
# print(df)
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test=train_test_split(df.drop('target',axis='columns'),df.target,test_size=0.2)
from sklearn.svm import SVC
rbf_model=SVC(kernel='rbf')
rbf_model.fit(x_train,y_train)
accuracy = rbf_model.score(x_test,y_test)
print("accuracy of model(using kernel=rbf):",accuracy)
linear_model = SVC(kernel='linear')
linear_model.fit(x_train,y_train)
accuracy=linear_model.score(x_test,y_test)
print("accuracy of model(using kernel=linear):",accuracy)