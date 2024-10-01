# 3. **Boolean Indexing** 
# Create a 4x4 NumPy array with random integers between 1 and 20. Use 
# Boolean indexing to: - Find and print all elements greater than 10. - Replace all elements less than 5 with 0. - Create a Boolean mask to identify all elements that are even numbers.
import numpy as np  

# Create a 4x4 array with random integers between 1 and 20  
array = np.random.randint(1, 21, size=(4, 4))  

# Print the original array  
print("Original Array:")  
print(array)  

# Find and print all elements greater than 10  
greater_than_10 = array[array > 10]  
print("\nElements greater than 10:")  
print(greater_than_10)  

# Replace all elements less than 5 with 0  
array[array < 5] = 0  
print("\nArray after replacing elements less than 5 with 0:")  
print(array)  

# Create a Boolean mask for even numbers  
even_mask = (array % 2 == 0)  
print("\nBoolean mask for even numbers:")  
print(even_mask)