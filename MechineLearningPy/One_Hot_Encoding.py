import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("carprices.csv")
dammies = pd.get_dummies(df["Car Model"])
merge = pd.concat([df,dammies],axis='columns')
final = merge.drop(["Car Model","Mercedez Benz C class"],axis='columns')
x= final.drop('Sell Price($)', axis='columns')
y= final['Sell Price($)']

# creat a liner regration class object:

reg = LinearRegression()
reg.fit(x,y)
print(reg.score(x,y))
print(reg.predict([[45000,4,0,0]]))
print(reg.predict([[86000,7,0,1]]))