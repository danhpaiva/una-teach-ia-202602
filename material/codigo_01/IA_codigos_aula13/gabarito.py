"""Gabarito da Aula 13 - exercicios 1 a 4 (autocontido)."""
import gymnasium as gym
import numpy as np


def retorno(rs, gamma):
    return sum(r * gamma ** t for t, r in enumerate(rs))


def treinar(env, episodios, alfa=0.1, gamma=0.99, eps0=1.0, eps_min=0.05,
            decaimento=0.999, seed=0):
    rng = np.random.default_rng(seed)
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    eps = eps0
    for ep in range(episodios):
        s, _ = env.reset(seed=int(rng.integers(1_000_000)))
        fim = False
        while not fim:
            if rng.random() < eps:
                a = int(rng.integers(env.action_space.n))
            else:
                a = int(Q[s].argmax())
            s2, r, term, trunc, _ = env.step(a)
            alvo = r + (0 if term else gamma * Q[s2].max())
            Q[s, a] += alfa * (alvo - Q[s, a])
            s, fim = s2, term or trunc
        eps = max(eps_min, eps * decaimento)
    return Q


def taxa_sucesso(env, Q, n=1000, seed=123):
    ok = 0
    for i in range(n):
        s, _ = env.reset(seed=seed + i)
        fim = False
        while not fim:
            s, r, term, trunc, _ = env.step(int(Q[s].argmax()))
            fim = term or trunc
        ok += r
    return ok / n


print("Exercicio 1 (retorno com desconto)")
for gamma in (0.5, 0.9):
    print("gamma", gamma, "->", round(retorno([1, 1, 1, 10], gamma), 3))

print("\nExercicio 2 (uma atualizacao de Q a mao)")
alfa, gamma = 0.5, 0.9
q, r, melhor = 2.0, 1.0, 4.0
alvo = r + gamma * melhor
print("alvo", alvo, " erro", round(alvo - q, 3),
      " Q novo", round(q + alfa * (alvo - q), 3))

print("\nExercicio 3 (FrozenLake escorregadio: episodios de treino)")
env = gym.make("FrozenLake-v1", is_slippery=True)
for n in (500, 2000, 5000, 20000):
    print(n, "episodios ->", taxa_sucesso(env, treinar(env, n)))

print("\nExercicio 4 (efeito de gamma no FrozenLake sem escorregar)")
env = gym.make("FrozenLake-v1", is_slippery=False)
for g in (0.0, 0.5, 0.9, 0.99):
    print("gamma", g, "->", taxa_sucesso(env, treinar(env, 3000, gamma=g)))
