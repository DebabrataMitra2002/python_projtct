import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df =pd.read_csv("insurance.csv")
plt.scatter(df.age,df.have_insurance,marker="+",color="red")
# df.plot(kind="scatter",y="have_insurance",x="age")
plt.show()
x_train,x_test,y_train,y_test= train_test_split(df[["age"]],df.have_insurance, test_size=0.1)
modle = LogisticRegression()
modle.fit(x_train,y_train)
print(modle.predict(x_test))
print(modle.score(x_test,y_test))

