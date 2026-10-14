def f(x):
    return (x - 3) ** 2 + 2

def df(x):
    return 2 * (x - 3)

def descer(alfa, passos=20, x=0.0):
    for _ in range(passos):
        x = x - alfa * df(x)
    return x

for alfa in [0.01, 0.1, 0.9, 1.1]:
    x = descer(alfa)
    print(alfa, round(x, 4), round(f(x), 4))
