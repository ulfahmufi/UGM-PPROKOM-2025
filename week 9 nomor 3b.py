import numpy as np

A = np.array([[2, 4, 6],
              [1, 3, 5]])

B = np.array([[1, 1, 1],
              [2, 2, 2]])

BT = B.T

perkalian = np.dot(A, BT)

print("Transpose B:\n", BT)
print("\nHasil A X B^T:\n", perkalian)