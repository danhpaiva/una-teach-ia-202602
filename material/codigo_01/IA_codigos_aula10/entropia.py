from collections import Counter
from math import log2
from dados_tenis import DADOS, ATRIBUTOS

def entropia(rotulos):
    n = len(rotulos)
    return -sum((c / n) * log2(c / n) for c in Counter(rotulos).values()) + 0.0

def gini(rotulos):
    n = len(rotulos)
    return 1 - sum((c / n) ** 2 for c in Counter(rotulos).values())

def ganho(dados, i):
    total = entropia([d[-1] for d in dados])
    resto = 0
    for valor in set(d[i] for d in dados):
        sub = [d[-1] for d in dados if d[i] == valor]
        resto += len(sub) / len(dados) * entropia(sub)
    return total - resto

if __name__ == "__main__":
    rot = [d[-1] for d in DADOS]
    print("sim/nao:", Counter(rot))
    print("entropia:", round(entropia(rot), 3), "gini:", round(gini(rot), 3))
    for i, nome in enumerate(ATRIBUTOS):
        print(f"ganho({nome}) = {ganho(DADOS, i):.3f}")
    for v in ("ensolarado", "nublado", "chuvoso"):
        sub = [d[-1] for d in DADOS if d[0] == v]
        print(v, Counter(sub), round(entropia(sub), 3))
