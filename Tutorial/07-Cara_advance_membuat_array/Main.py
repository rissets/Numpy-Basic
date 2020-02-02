import numpy as np

# Membuat matrik dengan tipe data tertentu (int, float, boolean, str)
a = np.array(([1,2,3], [4,5,6]), dtype = str)

# Membuat array dengan function
def kuadrat(baris,kolom):
    return kolom**2

b = np.fromfunction(kuadrat, (1,5), dtype = int)

def jumlah(baris,kolom):
    return (baris + kolom)

c = np.fromfunction(jumlah, (5,5), dtype = int)

# Membuat array atau matrix dengan menggunakan iterable
iterable = (x*x for x in range(10))

d = np.fromiter(iterable, dtype = int)


kali2 = (x*2 for x in range(5))

f = np.fromiter(kali2, dtype = int)

# Multiple array
dtype = [('nama', 'S225'), ('tinnggi', int)]

data = [
    ('wowok', 160),
    ('tengek', 180),
    ('darkom', 160)
]

g = np.array(data, dtype = dtype)

print(g)