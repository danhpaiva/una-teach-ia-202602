import numpy as np
from grad2d import gradiente

# Exercicio 1: derivada de x**3 em x = 2 (analitica: 3 * 2**2 = 12)
g = lambda x: x ** 3
h = 1e-5
print("ex1:", (g(2 + h) - g(2 - h)) / (2 * h))

# Exercicio 2: minimizar (x + 2)**2 + 1, x inicial 5, alfa 0.2 (minimo em x = -2)
x = 5.0
for _ in range(30):
    x = x - 0.2 * 2 * (x + 2)
print("ex2:", round(x, 4), "f(x) =", round((x + 2) ** 2 + 1, 4))

# Exercicio 3: regressao com varios alfas
xs = np.array([1, 2, 3, 4, 5, 6], dtype=float)
ys = np.array([2.1, 3.9, 6.2, 7.8, 10.1, 12.2])
n = len(xs)
for alfa in (0.02, 0.05, 0.1):
    w = b = 0.0
    for _ in range(500):
        erro = w * xs + b - ys
        w -= alfa * 2 / n * (erro * xs).sum()
        b -= alfa * 2 / n * erro.sum()
        if not np.isfinite(w):
            break
    print(f"ex3: alfa={alfa}: w={w:.4g}, b={b:.4g}")

# Exercicio 4: gradiente de x**2 + 3xy + y**2 em (1, 2): analitico [8, 7]
def f4(p):
    x, y = p
    return x ** 2 + 3 * x * y + y ** 2

print("ex4:", gradiente(f4, np.array([1.0, 2.0])))
