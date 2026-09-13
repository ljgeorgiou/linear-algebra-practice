import numpy as np

# From Scratch - No Numpy

v1 = [1, 2, 3]
v2 = [4, 5, 6]
m1 = [[1, 2, 3],
      [4, 5, 6]]

m2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

def add_vector(a: list[int], b: list[int]) -> list[int]:
    result: list[int] = []
    for e1, e2 in zip(a, b):
        result.append(e1 + e2)
    return result

print(add_vector(v1, v2)) # [5, 7, 9]

def dot_product(a: list[int], b: list[int]) -> int:
    total = 0
    for e1, e2 in zip(a, b):
        total += (e1 * e2)

    return total

print(dot_product(v1, v2)) #32

def matrix_times_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    result: list[int] = []

    for row in matrix:
        result.append(dot_product(row, vector))

    return result

print(matrix_times_vector(m1, v1)) # [14, 32]
print(matrix_times_vector(m2, v1)) # [14, 32, 50]

## The same thing using Numpy

nv1 = np.array([1, 2, 3])
nv2 = np.array([4, 5, 6])
nm1 = np.array([[1, 2, 3],
              [4, 5, 6]])

nm2 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

print(nv1 + nv2) #[5, 7, 9]
print(np.dot(nv1, nv2)) #32
print(nm1 @ nv1) #[14 32]
print(nm2 @ nv1) #[14 32 50]