def f(x):
    return x ** 4 - 3 * x ** 2 + x

def df(x):
    return 4 * x ** 3 - 6 * x + 1

for x0 in [-2.0, 0.5, 2.0]:
    x = x0
    for _ in range(200):
        x = x - 0.01 * df(x)
    print(x0, round(x, 3), round(f(x), 3))
