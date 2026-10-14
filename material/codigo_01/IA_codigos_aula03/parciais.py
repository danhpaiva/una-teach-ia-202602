def f(x, y):
    return x ** 2 + 3 * x * y

h = 1e-6
x, y = 1.0, 2.0
fx = (f(x + h, y) - f(x - h, y)) / (2 * h)
fy = (f(x, y + h) - f(x, y - h)) / (2 * h)
print(round(fx, 3), round(fy, 3))
