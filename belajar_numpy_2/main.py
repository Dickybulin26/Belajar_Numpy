import numpy as np

# membuat vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5 , 2.5, 5, 6, 7])
print(a)
print(b)

# membuat vektor dengan range
c = np.arange(1,10,0.2)

# membuat linspace
d = np.linspace(1,10,4) 

# membuat matriks
e = np.array([(1,2,3),(4,5,6)])

# matriks dengan nilai nol 
f = np.zeros((5,5))

# membuat dengan nilai satu
g = np.ones((5,5))

# membuat matriks identitas
h1 = np.identity(5)
h2 = np.eye(5)

# display
print("Belajar Matriks")
print(f"{a}\n\n,{b}\n\n,{c}\n\n,{d}\n\n,{e}\n\n,{f}\n\n,{g}\n\n,{h1}\n\n,{h2}")