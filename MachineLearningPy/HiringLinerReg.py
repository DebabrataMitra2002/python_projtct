import pandas as pd
from sklearn import linear_model as lm
from word2number import w2n 
import math

# Read the data from the hiring.csv file:
df = pd.read_csv('hiring.csv')

# Print the DataFrame to check its contents:
print("Original DataFrame:")
print(df)

# Fill missing values in the 'experience' column with 'zero':
df.experience = df.experience.fillna('zero')

# Print the DataFrame again to check the changes:
print("DataFrame after filling missing values:")
print(df)

# Convert word representations of numbers in 'experience' column to numeric values:
df.experience = df.experience.apply(w2n.word_to_num)

# Fill missing values in 'test_score(out of 10)' column with the median value:
median_test_score = math.floor(df['test_score(out of 10)'].mean())
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(median_test_score)

# Print the final DataFrame after handling missing values:
print("Final DataFrame after handling missing values:")
print(df)

# Create a linear regression object:
reg = lm.LinearRegression()

# Train the linear regression model:
reg.fit(df[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], df['salary($)'])

# Predict the salary of employees:
print('Person 1 predicted salary is:', reg.predict([[2, 9, 6]]))
print('Person 2 predicted salary is:', reg.predict([[12, 10, 10]]))
