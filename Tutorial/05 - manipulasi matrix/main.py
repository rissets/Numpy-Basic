import numpy as np

a = np.array((
    [1, 2, 3],
    [4, 5, 6]
))
print(a)

# shape (untuk mengetahui ukuran matrix)
b = a.shape
print('ukuran matrix a =', b)

# transpose (untuk mengubah baris menjadi kolom tanpa merubah nilai a)
print('transpose matrix a:')
print(a.transpose())
print(np.transpose(a))
print(a.T)
print(a)
print('='*10)

# ravel (me flatten array, mejadikan matrix ke vektor baris, tanpa merubah nilai a)
print('flatten matrixa:')
print(a.ravel())
print(np.ravel(a))
print(a)
print('=' * 10)

# reshape (mengubah baris dan kolom atau ukuran matrix, tanpa merubah nilai a ataupun ukuran nlai a)
print('reshape matrix a:')
print(a.reshape(3, 2))
print(a)
print('=' * 10)
'''
NB : untuk me reshape ukuranya harus sama dengan ukuran aslinya,
     perbedaan reshape dengan transpose adalah
     reshape = merubah nilai kolom dan barisnya sesuai dengan urutan nilai yang pertama
     transpose = merubah kolom menjadi baris, baris menjadi kolom
'''
# resize (merubah ukuran matrik serta merubah nilainya)
print('nilai a sebulum di resize =', a.shape)
a.resize(3, 2)
print(a)
print('nilai a sesudah di resize =', a.shape)
