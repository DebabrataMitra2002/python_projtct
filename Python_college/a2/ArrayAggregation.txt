# 9. **Array Aggregation** 
# Create a 4x4 matrix with random integers from 0 to 100. Perform the 
# following: - Compute the sum of all elements along each row. - Compute the sum of all elements along each column. - Compute the total sum of all elements in the matrix and normalize it by 
# dividing each element by this total sum. 
import numpy as np

# Create a 4x4 matrix with random integers from 0 to 100
matrix = np.random.randint(0, 101, size=(4, 4))

# 1. Compute the sum of all elements along each row
sum_along_rows = np.sum(matrix, axis=1)

# 2. Compute the sum of all elements along each column
sum_along_columns = np.sum(matrix, axis=0)

# 3. Compute the total sum of all elements in the matrix
total_sum = np.sum(matrix)

# Normalize the matrix by dividing each element by the total sum
normalized_matrix = matrix / total_sum

# Display the results
print("Original Matrix:")
print(matrix)

print("\nSum of elements along each row:")
print(sum_along_rows)

print("\nSum of elements along each column:")
print(sum_along_columns)

print("\nTotal sum of all elements in the matrix:")
print(total_sum)

print("\nNormalized Matrix:")
print(normalized_matrix)
