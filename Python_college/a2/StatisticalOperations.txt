#5. **Statistical Operations** 
# Create a NumPy array with 50 random integers between 10 and 100. 
# Compute: - The median of the array. - The variance of the array. - The 25th and 75th percentiles. - The number of elements that are greater than the mean value.
import numpy as np

# Create a NumPy array with 50 random integers between 10 and 100
random_array = np.random.randint(10, 100, size=50)

# Compute the median of the array
median_value = np.median(random_array)

# Compute the variance of the array
variance_value = np.var(random_array)

# Compute the 25th and 75th percentiles
percentile_25 = np.percentile(random_array, 25)
percentile_75 = np.percentile(random_array, 75)

# Compute the number of elements that are greater than the mean value
mean_value = np.mean(random_array)
elements_greater_than_mean = np.sum(random_array > mean_value)

# Display the results
print("Random Array:")
print(random_array)
print("\nMedian of the array:")
print(median_value)
print("\nVariance of the array:")
print(variance_value)
print("\n25th percentile of the array:")
print(percentile_25)
print("\n75th percentile of the array:")
print(percentile_75)
print("\nNumber of elements greater than the mean value:")
print(elements_greater_than_mean)
 