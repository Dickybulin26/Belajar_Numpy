import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10] 

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# elementwise opseration
# penjumlahan
hasil1 = anp + bnp

# pengurangan
hasil2 = anp-bnp

# perkalian
hasil3 = anp*bnp

# pembagian
hasil4 = anp/bnp

# kuadrat
hasil5 = anp+bnp**2

# matriks
c = np.array([(1,2,3),(4,5,6)])
d = np.array([(7,8,9),(-1,-2,-3)])

hasil6 = c+d
hasil7 = c*d

print (hasil7)