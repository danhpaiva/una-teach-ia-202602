def f(x):
    return x ** 2

def derivada_central(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

print(derivada_central(f, 3))
