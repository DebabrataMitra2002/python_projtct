# 2. **Array Reshaping and Indexing** 
# Generate a 1D array of 15 elements with values ranging from 0 to 14. 
# Reshape this array into a 3x5 matrix. Perform the following: 
import numpy as np  

# Generate a 1D array of 15 elements ranging from 0 to 14  
array_1d = np.arange(15)  

# Reshape the array into a 3x5 matrix  
matrix_2d = array_1d.reshape(3, 5)  

# Access and print the element in the second row and fourth column  
element = matrix_2d[1, 3]  
print("Element in second row and fourth column:", element)  

# Extract and print the first two rows of the matrix  
first_two_rows = matrix_2d[:2, :]  
print("First two rows of the matrix:\n", first_two_rows)  

# Flatten the reshaped matrix back to a 1D array  
flattened_array = matrix_2d.flatten()  
print("Flattened array:", flattened_array)