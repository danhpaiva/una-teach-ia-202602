import io
import random
from contextlib import redirect_stdout

import ga_onemax as g
import mochila as m
import pso
import tsp

# Exercicio 1: OneMax com e sem mutacao (media de 30 execucoes)
def rodar(p_mut, tam, seed, geracoes=40):
    random.seed(seed)
    g.P_MUT, g.TAM_POP = p_mut, tam
    pop = [g.criar_individuo() for _ in range(tam)]
    for _ in range(geracoes):
        melhor = max(pop, key=g.fitness)
        nova = [melhor]
        while len(nova) < tam:
            filho = g.crossover(g.torneio(pop), g.torneio(pop))
            nova.append(g.mutar(filho))
        pop = nova
    return g.fitness(max(pop, key=g.fitness))

def media(p_mut, tam=20):
    return sum(rodar(p_mut, tam, s) for s in range(30)) / 30

print("ex1:")
for p in [0.0, 1 / 30, 0.2, 0.5]:
    print(f"  p_mut={p:.3f} -> {media(p):.1f}")

# Exercicio 2: mochila com capacidade 30
m.CAPACIDADE = 30
otimo = m.forca_bruta()
print("ex2: otimo =", m.avaliar(otimo))
acertos = 0
for seed in range(20):
    random.seed(seed)
    acertos += m.avaliar(m.ga()) == m.avaliar(otimo)
print("     GA igual ao otimo em", acertos, "de 20")

# Exercicio 3: rota ingenua 0, 1, 2, ..., 9
print("ex3:", round(tsp.comprimento(list(range(10))), 2))

# Exercicio 4: inercia W no PSO (semente 7)
print("ex4:")
for w in (0.4, 0.7, 0.9):
    pso.W = w
    random.seed(7)
    with redirect_stdout(io.StringIO()):
        melhor = pso.pso()
    print(f"  W={w}: f = {pso.rastrigin(*melhor):.4f}")
