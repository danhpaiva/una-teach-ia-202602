import numpy as np

notas = np.array([7.5, 8.0, 5.5, 9.0, 6.0])
print(notas.mean(), notas.max())   # 7.2 9.0
print(notas[notas >= 7])           # [7.5 8.  9. ]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))                # 32

m = np.arange(6).reshape(2, 3)
print(m.shape, m.T.shape)          # (2, 3) (3, 2)
