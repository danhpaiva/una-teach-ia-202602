def y(x):
    return (x ** 2 + 1) ** 3

def derivada(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

x = 1
analitica = 3 * (x ** 2 + 1) ** 2 * 2 * x
print(analitica)
print(derivada(y, x))
