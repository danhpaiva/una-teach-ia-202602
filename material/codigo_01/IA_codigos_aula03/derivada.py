def f(x):
    return x ** 2

def derivada(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

print(derivada(f, 3))
print(derivada(f, 0))
print(derivada(f, -2))
