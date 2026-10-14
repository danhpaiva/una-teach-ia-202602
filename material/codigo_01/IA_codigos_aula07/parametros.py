import random
import ga_onemax as g

def rodar(p_mut, tam, elitismo=True, seed=0, geracoes=40):
    random.seed(seed)
    g.P_MUT, g.TAM_POP = p_mut, tam
    pop = [g.criar_individuo() for _ in range(tam)]
    for _ in range(geracoes):
        melhor = max(pop, key=g.fitness)
        nova = [melhor] if elitismo else []
        while len(nova) < tam:
            filho = g.crossover(g.torneio(pop), g.torneio(pop))
            nova.append(g.mutar(filho))
        pop = nova
    return g.fitness(max(pop, key=g.fitness))

def media(**kw):
    return sum(rodar(seed=s, **kw) for s in range(30)) / 30

for p in [0.0, 1 / 30, 0.2, 0.5]:
    print(f"p_mut={p:.3f}: {media(p_mut=p, tam=20):.1f}")
for t in [4, 20, 100]:
    print(f"tam_pop={t}: {media(p_mut=1/30, tam=t):.1f}")
print("sem elitismo:", round(media(p_mut=1/30, tam=20, elitismo=False), 1))
print("com elitismo:", round(media(p_mut=1/30, tam=20, elitismo=True), 1))
