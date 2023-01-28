import numpy as np

a = np.array(([1,2,3],[4,5,6]))

print('matrix a dengan ukuran: ',a.shape)
print(a)

# transpose matriks
print('transponse matrix dari a:')
print("\n",a.transpose())
print("\n",np.transpose(a))
print('\n',a.T)

# flatten array (vector baris)
print('flatten matrikx a:')
print("\n",a.ravel())
print("\n",np.ravel(a))

# reshape matrix
print('reshape matrikx a:')
print("\n",a.reshape(3,2))

# resize matrix
print('resize matrikx a:')
a.resize(3,2)
print("\n",a)
print("\n",a.reshape(3,2))