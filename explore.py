import numpy as np

# Adding two Vectors
v = np.array([1, 2, 3])
w = np.array([4, 5, 6])

print (v + w) # [5, 7, 9]

# Scaling a Vector
print(3 * v) # [3, 6, 9]

# Dot product 
print(np.dot(v, w)) # 32

# Length/Norm of a vector
print(np.linalg.norm(v)) #3.7 (1.d.p)
a = np.array([3, 4])
print(np.linalg.norm(a)) #5.0

# Building a Matrix
m = np.array([[1, 2, 3],
              [4, 5, 6]])

print(m.shape) # Gives the size of the matrix (2, 3)
print(m.T) # Transpose the matrix  [[1, 4],
           #                        [2, 5],
           #                        [3, 6]]

# Multiplying Matrices

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[4, 5],
              [6, 7]])

AB = (A @ B)  # [[16, 19],
              #  [36, 43]]
print(AB)

# Matrix times vector

C = [8, 9]
AC = (A @ C)
print(AC) # [26 60]