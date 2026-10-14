from itertools import product

def classificar(formula, n):
    linhas = product([True, False], repeat=n)
    valores = [formula(*v) for v in linhas]
    if all(valores):
        return "tautologia"
    if not any(valores):
        return "contradicao"
    return "contingencia"

print(classificar(lambda p: p or not p, 1))
print(classificar(lambda p: p and not p, 1))
print(classificar(lambda p, q: (not p) or q, 2))
