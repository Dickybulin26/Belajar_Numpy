import numpy as np

a = np.array(([1,2],
              [3,4]))
b = np.ones([2,2])

print(f"matriks a = \n{a}")
print(f"matriks b = \n{b}")

# perkalian matrix 
c = a*b
d = np.dot(a,b)
e = a.dot(b)

print(f"matriks b = \n{c}")
print(f"matriks b = \n{d}")
print(f"matriks b = \n{e}")