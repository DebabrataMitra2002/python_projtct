# 8. **Element-wise Operations** 
# Create two NumPy arrays A and B of the same shape. Perform the 
# following operations: - Compute the element-wise addition and subtraction of A and B. - Calculate the element-wise maximum and minimum values between A 
# and B. - Compute the Euclidean distance between the corresponding elements of 
# A and B.
import numpy as np

# Create two NumPy arrays A and B of the same shape (for example, 3x3 arrays)
A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3, 3))

# 1. Compute the element-wise addition and subtraction of A and B
element_wise_addition = A + B
element_wise_subtraction = A - B

# 2. Calculate the element-wise maximum and minimum values between A and B
element_wise_maximum = np.maximum(A, B)
element_wise_minimum = np.minimum(A, B)

# 3. Compute the Euclidean distance between the corresponding elements of A and B
euclidean_distance = np.sqrt((A - B) ** 2)

# Display the results
print("Array A:")
print(A)
print("\nArray B:")
print(B)

print("\nElement-wise Addition of A and B:")
print(element_wise_addition)

print("\nElement-wise Subtraction of A and B:")
print(element_wise_subtraction)

print("\nElement-wise Maximum between A and B:")
print(element_wise_maximum)

print("\nElement-wise Minimum between A and B:")
print(element_wise_minimum)

print("\nEuclidean Distance between corresponding elements of A and B:")
print(euclidean_distance)

