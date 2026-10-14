from itertools import product

def equivalentes(f, g, n):
    linhas = product([True, False], repeat=n)
    return all(f(*v) == g(*v) for v in linhas)

demorgan = equivalentes(lambda p, q: not (p and q),
                        lambda p, q: (not p) or (not q), 2)
inversa = equivalentes(lambda p, q: (not p) or q,
                       lambda p, q: (not q) or p, 2)
print(demorgan, inversa)
