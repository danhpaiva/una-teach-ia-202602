import numpy as np

x = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1, 12.2])

w, b = 0.0, 0.0
alfa = 0.02
n = len(x)

for epoca in range(1, 501):
    y_prev = w * x + b
    erro = y_prev - y
    custo = (erro ** 2).mean()
    dw = 2 / n * (erro * x).sum()
    db = 2 / n * erro.sum()
    w = w - alfa * dw
    b = b - alfa * db
    if epoca in (1, 10, 100, 500):
        print(epoca, round(w, 3), round(b, 3), round(custo, 4))

w, b = np.polyfit(x, y, 1)
print(round(w, 3), round(b, 3))
