import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model as lm


# print(pd.__version__)
# print(plt.__version__)
# print(np.__version__)


# print(pd.__path__)


# a=[12,34,45]
# myVar=pd.Series(a)
# print(myVar)


# print(pd.Series(a,index=["a","b","c"]))

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)

""" DataFrames
 Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

 Series is like a column, a DataFrame is the whole table """

# myDataset= {
#     'name':["debo","dola","baban"],
#     'marks':[12,23,34]
# }
# print(pd.DataFrame(myDataset))


# Load data csv file to data frame:
df = pd.read_csv('data.csv')
print(df.to_string())
print(df)
df.plot(kind='scatter',x='Duration',y='Pulse')
print(df.corr())
plt.show()
# print(df.info())
 
# x=np.array([0,8])
# y=np.array([0,8])
# plt.plot(x,y,marker='h',color='red',ls=':')
# plt.show()