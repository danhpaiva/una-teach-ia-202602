import random

N = 30            # genes por individuo
TAM_POP = 20
GERACOES = 40
P_MUT = 1 / N

def fitness(ind):
    return sum(ind)

def criar_individuo():
    return [random.randint(0, 1) for _ in range(N)]

def torneio(pop, k=3):
    return max(random.sample(pop, k), key=fitness)

def crossover(pai, mae):
    corte = random.randint(1, N - 1)
    return pai[:corte] + mae[corte:]

def mutar(ind):
    return [1 - g if random.random() < P_MUT else g for g in ind]

def evoluir():
    pop = [criar_individuo() for _ in range(TAM_POP)]
    for ger in range(GERACOES + 1):
        melhor = max(pop, key=fitness)
        if ger % 5 == 0:
            media = sum(map(fitness, pop)) / len(pop)
            print(f"ger {ger:2}: melhor={fitness(melhor)} media={media:.1f}")
        if fitness(melhor) == N:
            print(f"otimo na geracao {ger}")
            break
        nova = [melhor]
        while len(nova) < TAM_POP:
            filho = crossover(torneio(pop), torneio(pop))
            nova.append(mutar(filho))
        pop = nova
    return melhor

if __name__ == "__main__":
    random.seed(42)
    print(evoluir())
