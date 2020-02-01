import numpy as np
'''
Stacking Matrik: menumpuk matrik baik secara horizontal
maupun secara vertikal.
dengan menggunakan hstack untuk horisontal
dan vstack untuk vertikal
'''

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

am = np.ones((2,2))
bm = np.zeros((2,2))

# Stacking Matrik
c = np.hstack((a,b))
d = np.vstack((a,b))

cm = np.hstack((am,bm))
dm = np.vstack((am,bm))

# Output
print(c, 'Horizontal')
print(d, 'Vertikal')

print(cm, 'Horizontal')
print(dm, 'Vertikal')