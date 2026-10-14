from collections import Counter
from dados_tenis import DADOS, ATRIBUTOS
from entropia import ganho

def id3(dados, atributos):
    rotulos = [d[-1] for d in dados]
    if len(set(rotulos)) == 1:
        return rotulos[0]
    if not atributos:
        return Counter(rotulos).most_common(1)[0][0]
    def valor(a):
        return ganho(dados, ATRIBUTOS.index(a))
    melhor = max(atributos, key=valor)
    i = ATRIBUTOS.index(melhor)
    resto = [a for a in atributos if a != melhor]
    galhos = {}
    for valor in sorted(set(d[i] for d in dados)):
        sub = [d for d in dados if d[i] == valor]
        galhos[valor] = id3(sub, resto)
    return (melhor, galhos)

def prever(arvore, exemplo):
    while isinstance(arvore, tuple):
        atributo, galhos = arvore
        arvore = galhos[exemplo[atributo]]
    return arvore

def mostrar(arvore, recuo=0):
    if not isinstance(arvore, tuple):
        print("  " * recuo + "->", arvore)
        return
    atributo, galhos = arvore
    for valor, sub in galhos.items():
        print("  " * recuo + f"{atributo} = {valor}")
        mostrar(sub, recuo + 1)

if __name__ == "__main__":
    arvore = id3(DADOS, ATRIBUTOS)
    mostrar(arvore)
    novo = {"tempo": "ensolarado", "temperatura": "frio",
            "umidade": "alta", "vento": "forte"}
    print(prever(arvore, novo))
    acertos = sum(prever(arvore, dict(zip(ATRIBUTOS, d))) == d[-1] for d in DADOS)
    print(acertos, "de", len(DADOS))
