import numpy as np

X = np.array([1, 2])
print(X.shape)

W = np.array([[1, 2], [3, 4], [5, 6]])
print(W.shape)

Y = np.dot(W, X)
print(Y.shape)

print(Y)
