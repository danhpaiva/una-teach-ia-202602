from itertools import product

def equivalentes(f, g, n):
    linhas = product([True, False], repeat=n)
    return all(f(*v) == g(*v) for v in linhas)

def entails(kb, alpha, simbolos):
    for valores in product([True, False], repeat=len(simbolos)):
        modelo = dict(zip(simbolos, valores))
        if kb(modelo) and not alpha(modelo):
            return False
    return True

# Exercicio 1: tabela-verdade de (p E q) -> r
print("ex1:")
for p, q, r in product([True, False], repeat=3):
    print(" ", p, q, r, (not (p and q)) or r)
# (so e falsa em (True, True, False): 1 linha em 8)

# Exercicio 2: p -> q equivale a q OU (nao p) (contrapositiva)
print("ex2:", equivalentes(lambda p, q: (not p) or q,
                           lambda p, q: q or (not p), 2))

# Exercicio 3: {p -> q, q -> r, p} implica r
def kb(m):
    a = (not m["p"]) or m["q"]
    b = (not m["q"]) or m["r"]
    return a and b and m["p"]

print("ex3:", entails(kb, lambda m: m["r"], "pqr"))

# Exercicio 4: avestruz na rede semantica
rede = {
    "animal":  {"tem": "pele"},
    "ave":     {"e_um": "animal", "voa": True, "tem": "penas"},
    "canario": {"e_um": "ave", "cor": "amarelo"},
    "pinguim": {"e_um": "ave", "voa": False},
}

def propriedade(no, prop):
    while no is not None:
        if prop in rede[no]:
            return rede[no][prop]
        no = rede[no].get("e_um")
    return None

rede["avestruz"] = {"e_um": "ave",
    "voa": False, "cor": "marrom"}
print("ex4:", propriedade("avestruz", "cor"), propriedade("avestruz", "voa"))
