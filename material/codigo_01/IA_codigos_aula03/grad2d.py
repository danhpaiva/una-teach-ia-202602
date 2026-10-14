import numpy as np

def f(p):
    x, y = p
    return x ** 2 + y ** 2

def gradiente(f, p, h=1e-6):
    g = np.zeros_like(p)
    for i in range(len(p)):
        passo = np.zeros_like(p)
        passo[i] = h
        g[i] = (f(p + passo) - f(p - passo)) / (2 * h)
    return g

if __name__ == "__main__":
    print(gradiente(f, np.array([3.0, 4.0])))
