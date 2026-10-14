import random
from itertools import product

ITENS = [("notebook", 30, 7), ("camera", 18, 4), ("livro", 6, 2),
         ("tenda", 25, 9), ("garrafa", 4, 1), ("jaqueta", 12, 5),
         ("fogareiro", 15, 3), ("lanterna", 8, 2), ("saco_dormir", 20, 8),
         ("mapa", 5, 1), ("kit_medico", 14, 3), ("binoculo", 10, 4)]
CAPACIDADE = 20

def avaliar(ind):
    valor = sum(g * it[1] for g, it in zip(ind, ITENS))
    peso = sum(g * it[2] for g, it in zip(ind, ITENS))
    return valor if peso <= CAPACIDADE else 0

def forca_bruta():
    todas = product([0, 1], repeat=len(ITENS))
    return max(todas, key=avaliar)

def ga(geracoes=60, tam=30, p_mut=0.05):
    n = len(ITENS)
    pop = [[random.randint(0, 1) for _ in range(n)] for _ in range(tam)]
    for _ in range(geracoes):
        melhor = max(pop, key=avaliar)
        nova = [melhor]
        while len(nova) < tam:
            a = max(random.sample(pop, 3), key=avaliar)
            b = max(random.sample(pop, 3), key=avaliar)
            corte = random.randint(1, n - 1)
            filho = a[:corte] + b[corte:]
            filho = [1 - g if random.random() < p_mut else g for g in filho]
            nova.append(filho)
        pop = nova
    return max(pop, key=avaliar)

if __name__ == "__main__":
    otimo = forca_bruta()
    print("forca bruta:", avaliar(otimo), otimo)
    random.seed(1)
    r = ga()
    print("GA        :", avaliar(r), r)
    acertos = 0
    for s in range(20):
        random.seed(s)
        acertos += avaliar(ga()) == avaliar(otimo)
    print("GA achou o otimo em", acertos, "de 20 execucoes")
