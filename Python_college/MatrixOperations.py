# Given two matrices, `A` (2x3) and `B` (3x2), perform the following operations: - Multiply `A` and `B` using matrix multiplication. - Compute the element-wise product of `A` and its transpose. 
# - Calculate the determinant of the resulting matrix from the element-wise 
# product.
import numpy as np

# Define matrices A and B
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

# 1. Matrix multiplication A * B
AB = np.dot(A, B)

# 2. Compute the element-wise product of A and its transpose (A * A^T)
A_transpose = A.T
AA_T = np.dot(A, A_transpose)

# 3. Calculate the determinant of the resulting matrix from the element-wise product
determinant_AA_T = np.linalg.det(AA_T)

# Display the results
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix Multiplication (A * B):")
print(AB)
print("\nElement-wise Product (A * A^T):")
print(AA_T)
print("\nDeterminant of the Element-wise Product matrix:")
print(determinant_AA_T)
