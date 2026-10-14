from itertools import product

def entails(kb, alpha, simbolos):
    n = len(simbolos)
    for valores in product([True, False], repeat=n):
        modelo = dict(zip(simbolos, valores))
        if kb(modelo) and not alpha(modelo):
            return False
    return True

def kb(m):
    return (((not m["chuva"]) or m["molhado"])
            and ((not m["molhado"]) or m["escorregadio"])
            and m["chuva"])

S = ["chuva", "molhado", "escorregadio", "sol"]
print(entails(kb, lambda m: m["escorregadio"], S))
print(entails(kb, lambda m: not m["escorregadio"], S))
print(entails(kb, lambda m: m["sol"], S))
