import numpy as np

'''
01 - vektor = bentik sederhana dari array, yang merupakan array satu dimensi.
02 - linear space = -
03 - matrix = susunan bilangan, simbol, atau ekspresi, yang disusun dalam baris dan kolom sehingga membentuk bilangan persegi,
              sehingga panjang dan lebarnya ditentukan dengan banyaknya kolom dan baris.
04 - matrix identitas = matrix persegi panjang n*n dengan angka" satu di diagonal utama dan nol ditempat lainya.
05 - matrix nol = matrix yang semua elemenya adalah nol(0)
'''
# memuat vektor
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([1.5, 3.5, 3.3])  # dengan koma

# membuat vektor dengan range
b1 = np.arange(1, 10, 2)  # mengambil nilai 1 - 10 dengan jarak 2 nilai
b2 = np.arange(1, 10, 4)  # dengan jarak 4

# membuat linear space (linspace)
c = np.linspace(1, 10, 4)  # mengambil 5 nilai dari 1 - 10 dengan jarak 4

# membuat multidimensi/matrix
# jumplah komponen antara kedua nilay harus sama
d = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])

# matrix dengan nilai nol
e = np.zeros((5, 5))

# matrix dengan nilai satu
f = np.ones((5, 5))

# matrix indentitas
g1 = np.identity(5)
g2 = np.eye(10)


# disply
print(g2)
