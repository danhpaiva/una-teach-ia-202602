def quente_crisp(t):
    return 1 if t >= 30 else 0

for t in [29.9, 30, 25, 35]:
    print(t, quente_crisp(t))
