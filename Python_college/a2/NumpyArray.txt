# Create a 3x3 NumPy array of integers from 1 to 9. Perform the following 
# operations:
import numpy as np  

# Create the 3x3 array  
array = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])  

# Compute the transpose of the array  
transpose_array = array.T  

# Calculate the sum of all elements in the array  
total_sum = np.sum(array)  

# Compute the mean of each column  
mean_columns = np.mean(array, axis=0)  

# Find the maximum value in the array  
max_value = np.max(array)  

# Print results  
print("Transpose of the array:\n", transpose_array)  
print("Sum of all elements:", total_sum)  
print("Mean of each column:", mean_columns)  
print("Maximum value in the array:", max_value)