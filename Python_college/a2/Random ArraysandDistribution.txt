# 6. **Random Arrays and Distribution** 
# Generate an array of 1000 elements from a normal distribution with a mean 
# of 0 and a standard deviation of 1. Perform the following: - Plot a histogram of the generated values. - Calculate the mean and standard deviation of the array. - Verify if the array follows the expected normal distribution by checking 
# the skewness and kurtosis (use appropriate NumPy or SciPy functions). 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# 1. Generate an array of 1000 elements from a normal distribution
normal_array = np.random.normal(loc=0, scale=1, size=1000)

# 2. Plot a histogram of the generated values
plt.hist(normal_array, bins=30, edgecolor='black')
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 3. Calculate the mean and standard deviation of the array
mean_value = np.mean(normal_array)
std_deviation = np.std(normal_array)

# 4. Calculate the skewness and kurtosis to verify normality
skewness = skew(normal_array)
kurt = kurtosis(normal_array)

# Display the results
print(f"Mean of the array: {mean_value}")
print(f"Standard Deviation of the array: {std_deviation}")
print(f"Skewness of the array: {skewness}")
print(f"Kurtosis of the array: {kurt}")
