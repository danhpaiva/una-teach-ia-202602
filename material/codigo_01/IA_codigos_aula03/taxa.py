def f(x):
    return x ** 2

for h in [1, 0.5, 0.1, 0.01, 0.001]:
    taxa = (f(1 + h) - f(1)) / h
    print(h, taxa)
