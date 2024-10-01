# 7. **Array Manipulation** 
# Create a 5x5 array filled with random integers between 1 and 10. Perform 
# the following tasks: - Replace all values in the central 3x3 subarray with the number 99. - Swap the first and last rows of the array. - Compute the sum of all values in the even-indexed columns. 
import numpy as np

# 1. Create a 5x5 array filled with random integers between 1 and 10
array = np.random.randint(1, 11, size=(5, 5))

# 2. Replace all values in the central 3x3 subarray with the number 99
array[1:4, 1:4] = 99

# 3. Swap the first and last rows of the array
array[[0, 4]] = array[[4, 0]]

# 4. Compute the sum of all values in the even-indexed columns
# Even-indexed columns are 0, 2, and 4 (assuming 0-based indexing)
sum_even_columns = np.sum(array[:, ::2])

# Display the results
print("Modified Array:")
print(array)
print("\nSum of values in even-indexed columns:")
print(sum_even_columns)

