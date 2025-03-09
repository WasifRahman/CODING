
#***Matrix(Two Dimentional List)
matrix = [
    [1,2,3],
    [4,5,6],
]
print(matrix[0][2]) #$Output:3 , 0 number row 2 number column

#! value change
matrix[0][2]=10
print(matrix[0][2]) #$Output:10 , value change

#! 
for row in matrix:
    for col in row:
        print(col) #$Output:1 2 3 4 5 6 niche niche
        

#*** What is a Matrix?
#?A matrix is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. In Python, matrices are typically represented as lists of lists or using specialized libraries like NumPy. Matrices are fundamental in linear algebra and serve as a powerful way to organize and manipulate data, solve systems of linear equations, and represent transformations.

#@ Matrix Code Example

import numpy as np
#! Creating a 3x3 matrix
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

#! Creating another matrix
matrix_b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

#$ Matrix addition
result_add = matrix_a + matrix_b
print("Matrix Addition:")
print(result_add)

#$ Matrix multiplication
result_mul = np.matmul(matrix_a, matrix_b)
print("\nMatrix Multiplication:")
print(result_mul)

#$ Transpose of a matrix
result_transpose = matrix_a.T
print("\nMatrix Transpose:")
print(result_transpose)


#*** Common Mistakes and Misconceptions

#? 1. **Confusing lists of lists with true matrices**: Python lists of lists don't support proper matrix operations like multiplication. Use NumPy arrays instead for actual matrix behavior.
#? 2. **Matrix multiplication misconception**: Matrix multiplication is not element-wise multiplication. The operation follows specific rules where dimensions must be compatible (the number of columns in the first matrix must equal the number of rows in the second).
#? 3. **Ignoring performance considerations**: Regular Python lists are inefficient for large matrices. NumPy provides optimized implementations that are significantly faster for matrix operations on large datasets.

#*** Real-World Applications
#? 1. **Computer Graphics and 3D Transformations**: Matrices represent rotations, translations, and scaling in 3D graphics. Game engines and graphics software use matrices to transform objects in virtual space.
#? 2. **Machine Learning and Data Analysis**: Matrices serve as the foundation for representing datasets, calculating covariance, performing dimensionality reduction (like PCA), and implementing algorithms like neural networks.

#*** Practice Exercises

#@============== Exercise 1: Basic Matrix Operations

#!Create two 2x2 matrices and perform addition, subtraction, and multiplication operations.

import numpy as np

#! Solution
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

#! Addition
print("Addition:", a + b)

#! Subtraction
print("Subtraction:", a - b)

#! Multiplication
print("Multiplication:", np.matmul(a, b))

#@=========== Exercise 2: Matrix Determinant and Inverse
#!Calculate the determinant and inverse of a matrix, then verify that multiplying a matrix by its inverse gives the identity matrix.

import numpy as np

#! Solution
matrix = np.array([[4, 7], [2, 6]])

#! Calculate determinant
det = np.linalg.det(matrix)
print("Determinant:", det)

#! Calculate inverse
inv = np.linalg.inv(matrix)
print("Inverse:", inv)

#! Verify: matrix × inverse ≈ identity matrix
result = np.matmul(matrix, inv)
print("Verification:", np.round(result, 10))  # Rounding to handle floating point errors


#@=========== Exercise 3: Linear System Solver
#!Use matrices to solve a system of linear equations like:
#$ 3x + 2y - z = 10
#$ 2x - 2y + 4z = -2
#$ -x + 0.5y - z = 0

import numpy as np

#! Solution
#! Coefficient matrix
A = np.array([
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
])

#! Constants vector
b = np.array([10, -2, 0])

#! Solve the system
solution = np.linalg.solve(A, b)
print("Solution (x, y, z):", solution)

#! Verify the solution
verification = np.matmul(A, solution)
print("Verification:", np.round(verification, 10))

#*** Thought-Provoking Question
#How might the concept of eigenvalues and eigenvectors of a matrix help us understand complex systems like social networks or ecosystems, and what insights could we gain by applying these mathematical tools to real-world problems that appear unrelated to mathematics?