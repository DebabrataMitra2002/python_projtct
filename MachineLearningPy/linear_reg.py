import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model as lm

# Read the dataset
df = pd.read_csv('homeprices.csv')

# Plotting the scatter graph with regression line using Seaborn
plt.figure(figsize=(10, 6))

sns.regplot(x='area', y='price', data=df,ci=None)

plt.xlabel('Area (sqr ft)')
plt.ylabel('Price (US$)')
plt.title('Area vs Price with Regression Line')

plt.show()

# Create a linear regression model object
reg = lm.LinearRegression()

# Prepare the data
X = df[['area']]  # Feature matrix
y = df['price']   # Target variable

# Train the model
reg.fit(X, y)

# Predict the price for a new area value of 3300 square feet
predicted_price = reg.predict([[3300]])
print("Predicted price for an area of 3300 sqft:", predicted_price)
