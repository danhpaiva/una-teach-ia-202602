import gymnasium as gym
import numpy as np

env = gym.make("Taxi-v4")
print("estados:", env.observation_space.n, " acoes:", env.action_space.n)
rng = np.random.default_rng(0)
Q = np.zeros((env.observation_space.n, env.action_space.n))
alfa, gamma, eps = 0.1, 0.99, 1.0
for ep in range(5000):
    s, _ = env.reset(seed=int(rng.integers(1_000_000)))
    fim = False
    while not fim:
        a = int(rng.integers(6)) if rng.random() < eps else int(Q[s].argmax())
        s2, r, term, trunc, _ = env.step(a)
        alvo = r + (0 if term else gamma * Q[s2].max())
        Q[s, a] += alfa * (alvo - Q[s, a])
        s, fim = s2, term or trunc
    eps = max(0.05, eps * 0.999)

def avaliar(politica, n=200):
    totais = []
    for i in range(n):
        s, _ = env.reset(seed=1000 + i)
        total, fim = 0, False
        while not fim:
            s, r, term, trunc, _ = env.step(politica(s))
            total, fim = total + r, term or trunc
        totais.append(total)
    return round(float(np.mean(totais)), 1)

print("agente aleatorio, retorno medio:", avaliar(lambda s: int(rng.integers(6))))
print("agente Q-learning, retorno medio:", avaliar(lambda s: int(Q[s].argmax())))
