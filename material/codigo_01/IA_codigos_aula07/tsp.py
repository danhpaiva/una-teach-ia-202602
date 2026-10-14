import math
import random
from itertools import permutations

CIDADES = [(0, 0), (2, 6), (5, 2), (6, 6), (8, 3),
           (1, 3), (4, 7), (7, 0), (9, 6), (3, 1)]

def dist(a, b):
    return math.dist(CIDADES[a], CIDADES[b])

def comprimento(rota):
    return sum(dist(rota[i], rota[(i + 1) % len(rota)])
               for i in range(len(rota)))

def cruzamento_ox(p1, p2):
    a, b = sorted(random.sample(range(len(p1)), 2))
    meio = p1[a:b]
    resto = [c for c in p2 if c not in meio]
    return resto[:a] + meio + resto[a:]

def mutar_troca(rota, p=0.2):
    rota = rota[:]
    if random.random() < p:
        i, j = random.sample(range(len(rota)), 2)
        rota[i], rota[j] = rota[j], rota[i]
    return rota

def ga_tsp(geracoes=150, tam=60):
    n = len(CIDADES)
    pop = [random.sample(range(n), n) for _ in range(tam)]
    for _ in range(geracoes):
        pop.sort(key=comprimento)
        nova = pop[:2]
        while len(nova) < tam:
            p1 = min(random.sample(pop, 3), key=comprimento)
            p2 = min(random.sample(pop, 3), key=comprimento)
            nova.append(mutar_troca(cruzamento_ox(p1, p2)))
        pop = nova
    return min(pop, key=comprimento)

def vizinho_mais_proximo():
    rota, livres = [0], set(range(1, len(CIDADES)))
    while livres:
        prox = min(livres, key=lambda c: dist(rota[-1], c))
        rota.append(prox)
        livres.remove(prox)
    return rota

if __name__ == "__main__":
    random.seed(3)
    aleatoria = min((random.sample(range(10), 10) for _ in range(1000)),
                    key=comprimento)
    print("melhor de 1000 aleatorias:", round(comprimento(aleatoria), 2))
    print("vizinho mais proximo     :", round(comprimento(vizinho_mais_proximo()), 2))
    rota = ga_tsp()
    print("GA                       :", round(comprimento(rota), 2), rota)
    exata = min(([0] + list(p) for p in permutations(range(1, 10))), key=comprimento)
    print("exata (9! rotas)         :", round(comprimento(exata), 2), exata)
