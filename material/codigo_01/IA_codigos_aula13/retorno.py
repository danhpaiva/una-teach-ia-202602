recompensas = [-1, -1, -1, 10]          # tres passos custam -1 e a meta paga 10

def retorno(rs, gamma):
    return sum(r * gamma ** t for t, r in enumerate(rs))

for gamma in (0.0, 0.5, 0.9, 1.0):
    g = retorno(recompensas, gamma)
    print("gamma", gamma, "-> retorno", round(g, 3))

print("valor de 1 ponto daqui a n passos (gamma = 0.9):")
for n in (0, 1, 5, 10, 20):
    print(" n =", n, "->", round(0.9 ** n, 3))
