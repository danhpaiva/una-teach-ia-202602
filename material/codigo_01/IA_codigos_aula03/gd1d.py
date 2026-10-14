def f(x):
    return (x - 3) ** 2 + 2

def df(x):
    return 2 * (x - 3)

x = 0.0
alfa = 0.1
for passo in range(1, 11):
    x = x - alfa * df(x)
    print(passo, round(x, 4), round(f(x), 4))
