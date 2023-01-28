import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

aMat = np.zeros((2,3))
bMat = np.zeros((2,3))


# stacking matrix (menumpuk matriks)

c = np.hstack((a, b))
d = np.vstack((a, b))

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))
print(c)
print(d)
print(cMat)
print(dMat)

