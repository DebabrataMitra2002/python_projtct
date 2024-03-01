import pandas as pd
from sklearn import linear_model as lm
import matplotlib.pyplot as plt

# Read the dataset

df = pd.read_csv('homeprices.csv')

# Plotting the scatter graph
plt.xlabel('area (sqr ft)')
plt.ylabel('prices (US$)')
plt.scatter(df.area, df.price, color='red', marker='+')
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
