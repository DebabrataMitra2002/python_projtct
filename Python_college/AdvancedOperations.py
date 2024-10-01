# 10. **Advanced Operations** 
# Generate a 6x6 matrix of random numbers between 0 and 1. Perform the 
# following: - Compute the cumulative sum along the columns. - Create a new matrix where each element is the logarithm (base 10) of the 
# corresponding element in the original matrix. - Determine the indices where the elements of the matrix are above a 
# threshold value (e.g., 0.5). 

import numpy as np

# Generate a 6x6 matrix of random numbers between 0 and 1
matrix = np.random.rand(6, 6)

# 1. Compute the cumulative sum along the columns
cumulative_sum_columns = np.cumsum(matrix, axis=0)

# 2. Create a new matrix where each element is the logarithm (base 10) of the corresponding element in the original matrix
# Use np.log10 and handle log(0) by setting such elements to a small number (since log(0) is undefined)
log_matrix = np.log10(np.where(matrix > 0, matrix, np.nextafter(0, 1)))

# 3. Determine the indices where the elements of the matrix are above a threshold value (e.g., 0.5)
threshold = 0.5
indices_above_threshold = np.argwhere(matrix > threshold)

# Display the results
print("Original Matrix:")
print(matrix)

print("\nCumulative Sum along Columns:")
print(cumulative_sum_columns)

print("\nMatrix with Logarithm (base 10) of Elements:")
print(log_matrix)

print("\nIndices of Elements above Threshold (0.5):")
print(indices_above_threshold)
