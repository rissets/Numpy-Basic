import numpy as np
'''
ELEMENTWISE oprations = operasi aritmetika yang dilakukan per komponen
NB : semua operasi dinumpy menggunakan ELEMENTWISE operations
'''
a = np.array([1, 2, 3, 4])
b = np.array([6, 7, 8, 9])

# penjumplahan
hasil = a + b

# pengurangan
hasil = a - b

# perkalian
hasil = a * b

# pembagian
hasil = b / a

# kuadrat
hasil = a ** 2

# multidimensi array numpy
c = np.array([(1, 2, 3, 4), (6, 7, 8, 9)])
d = np.array([(4, 3, 2, 1), (9, 8, 7, 6)])
hasil = c + d
hasil = c * d

print(hasil)
