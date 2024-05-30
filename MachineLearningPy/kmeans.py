from cProfile import label
from sklearn import preprocessing
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

df = pd.read_csv("income.csv")
# print(df.head())

# plt.scatter(df.Age,df['Income($)'])
# plt.show()

km=KMeans(n_clusters=3)
y_predict=km.fit_predict(df[['Age','Income($)']]) 
# print(y_predict)
df['cluster']=y_predict
# print(df.head())

# df1 =df[df.cluster==0]
# df2 =df[df.cluster==1]
# df3 =df[df.cluster==2]

# plt.scatter(df1.Age,df1['Income($)'],label='Income($)',color='red')
# plt.scatter(df2.Age,df2['Income($)'],label='Income($)',color='green')
# plt.scatter(df3.Age,df3['Income($)'],label='Income($)',color='black')
# plt.xlabel('Age')
# plt.ylabel('Income($)')
# plt.legend()
# plt.show()

# We need some preprocessing using MinMaxScaler 
scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])
# print(df.head())
scaler.fit(df[['Age']])
df.Age = scaler.transform(df[['Age']])
# print(df.head())

km_m = KMeans(n_clusters=3)
y_pre = km_m.fit_predict(df[['Age','Income($)']])
df['cluster2']=y_pre
print(km_m.cluster_centers_)
# print(df.head())

df1 =df[df.cluster2==0]
df2 =df[df.cluster2==1]
df3 =df[df.cluster2==2]


plt.scatter(df1.Age,df1['Income($)'],label='Income($)',color='red')
plt.scatter(df2.Age,df2['Income($)'],label='Income($)',color='green')
plt.scatter(df3.Age,df3['Income($)'],label='Income($)',color='black')
plt.scatter(km_m.cluster_centers_[: ,0],km_m.cluster_centers_[:,1],c='purple',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.legend()
plt.show()

# elbo method
sse = []
k_rng = range(1,10)
for k in k_rng:
    km_m = KMeans(n_clusters=k)
    km_m.fit(df[['Age','Income($)']])
    sse.append(km_m.inertia_)
plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)
plt.show()