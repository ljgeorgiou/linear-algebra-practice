import numpy as np

# Addition of two vectors

v1 = np.array([3, 4, 5])
v2 = np.array([6, 7, 8])

print(v1 + v2) # [9 11 13]

# Scaling a vector
v1_scaled = 5 * v1
print(v1_scaled) #[15 20 25]

# Dot product
print(np.dot(v1, v2))

# Transposing a matrix
m = np.array([[1, 2, 3],
              [4, 5, 6]])

m_t = m.T 
print(m_t)
