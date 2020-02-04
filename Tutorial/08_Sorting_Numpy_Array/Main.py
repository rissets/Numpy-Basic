import numpy as np
# Sorting satu dimensi
print("Sorting Satu Dimensi")

a = np.floor(np.random.randn(1,6)*10) # menghasilkan nilai random
print(a)
print("Nilai maxsimal dari a = ",a.max()) # untuk mengetahui nilai maksimum
print("Urutan posisi max a = ",a.argmax()) # mengetahui posisi nilai maksimum

print("Nilai minimum dari a = ",a.min()) # untuk mengetahui nilai minimum
print("Urutan posisi min a = ", a.argmin()) # mengetahui posisi nilai minimum

print("="*10)

print("mengurutkan nilai random a = ")
print(np.sort(a)) # kecil ke besar
print(np.argsort(a)) # mengetahui posisi dari kecil ke besar dan mengurutkannya
print("*"*90)

# Sorting Multi dimensi
print("Sorting Multi Dimensi")

b = np.floor(np.random.randn(3,3)*10) # menghasilkan nilai random
print(b)
print("Nilai maxsimal dari b = ",b.max()) # untuk mengetahui nilai maksimum
print("Urutan posisi max b = ",b.argmax()) # mengetahui posisi nilai maksimum

print("Nilai minimum dari b = ",b.min()) # untuk mengetahui nilai minimum
print("Urutan posisi min b = ", b.argmin()) # mengetahui posisi nilai minimum

print("="*10)

print("mengurutkan nilai random b = ")
print(np.sort(b)) # kecil ke besar
print(np.argsort(b)) # mengetahui posisi dari kecil ke besar dan mengurutkannya
print("*"*90)

# Sorting Costum array
print("Sorting Costum Array")

dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [
    ('Wowok', 160),
    ('Tengek', 180),
    ('Dobok', 150),
    ('Tarkom', 175),
]

a = np.array(data, dtype=dtipe)
print(a)

print(np.sort(a, order='tinggi')) # Sortir berdasarkan tinggi
print(np.sort(a, order='nama')) # Sortir berdasarkan nama