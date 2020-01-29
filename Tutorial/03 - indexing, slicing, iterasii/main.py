import numpy as np

a = np.arange(10) ** 2
print(a)

# Mengambil nilai
print('element ke 1 dari a adalah', a[0])
print('element ke 6 dari a adalah', a[6])
print('element terakhir dari a adalah', a[-1])

# Slicing (mengambil rentang nilai)
print('element dari 1 - 6 adalah', a[0:6])
print('element dari 5 sampai akhir', a[4:])
print('element awal sampai 6 adalah', a[:6])

# Iterasi
for i in a:
    print('value =', i)
