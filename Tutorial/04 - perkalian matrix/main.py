import numpy as np

# Perkalian matrix
'''
suatu operasi biner yang dapat menghasilkan sesuatu matrixs
dari dua matrix dengan entri dalam suatu medan tertentu,
atau secara lebih umum dalam suatu gelanggang
atau bahkan suatu semigelanggang.
'''

# sifat perkalian matrix
'''
baris dikali kolom
dalam perkalian matrix jumlah baris dan kolom dari kedua nilai harus sama
'''


a = np.array(([1, 2, 3], [3, 2, 1]))
b = np.ones([3, 2])

print(a)
print('='*10)
print(b)
print('='*10)

# perkalian matrix dengan menggunakan dot
c = np.dot(a, b)
c2 = a.dot(b)
print(c)
print('=' * 10)
print(c2)
