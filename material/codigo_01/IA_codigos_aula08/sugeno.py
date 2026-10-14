from pertinencia import tri

def potencia_sugeno(erro):
    graus = [float(tri(erro, -6, -6, 0)),
             float(tri(erro, -1.5, 0, 1.5)),
             float(tri(erro, 0, 2, 4)),
             float(tri(erro, 2, 6, 10))]
    saidas = [0, 25, 55, 100]   # uma constante por regra
    soma = sum(graus)
    if soma == 0:
        return 0.0
    return sum(g * s for g, s in zip(graus, saidas)) / soma

for e in [-3, 0, 1, 2, 4, 7]:
    print(e, round(potencia_sugeno(e), 1))
