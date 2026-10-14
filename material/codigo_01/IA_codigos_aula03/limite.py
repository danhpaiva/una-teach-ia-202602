def g(x):
    return (x ** 2 - 1) / (x - 1)

for h in [0.1, 0.01, 0.001]:
    print(1 - h, g(1 - h), 1 + h, g(1 + h))
