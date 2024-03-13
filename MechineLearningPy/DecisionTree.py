import pandas as pd


df=pd.read_csv('salaries.csv')
# print(df)

inputs = df.drop('salary_more_then_100k',axis='columns')
target= df['salary_more_then_100k']
# print(input)
# print(target)

from sklearn.preprocessing import LabelEncoder as LE
le_company=LE()
le_job=LE()
le_degree=LE()

inputs['company_n']=le_company.fit_transform(inputs['company'])
inputs['job_n']=le_job.fit_transform(inputs['job'])
inputs['degree_n']=le_degree.fit_transform(inputs['degree'])

# print(input)
input_n = inputs.drop(['company','job','degree'],axis='columns')

# print(input_n)

from sklearn import tree
model= tree.DecisionTreeClassifier()
model.fit(input_n,target)
print("Accuracy of this model is:",model.score(input_n,target))

# Is salary of Google, Computer Engineer, Bachelors degree > 100 k ?
print("Is salary of Google, Computer Engineer, Bachelors degree > 100 k ?(yes=[1]/no=[0]) :",model.predict([[2,1,0]]))

#Is salary of Google, Computer Engineer, Masters degree > 100 k ?

print("Is salary of Google, Computer Engineer, Masters degree > 100 k ?(yes=[1]/no=[0]) :",model.predict([[2,1,1]]))

