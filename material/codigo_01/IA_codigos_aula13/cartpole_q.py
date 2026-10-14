import gymnasium as gym
import numpy as np

env = gym.make("CartPole-v1")
limites = [(-2.4, 2.4), (-3.0, 3.0), (-0.21, 0.21), (-3.5, 3.5)]
bins = (6, 6, 12, 12)

def discretizar(obs):
    idx = []
    for x, (lo, hi), n in zip(obs, limites, bins):
        k = int((np.clip(x, lo, hi - 1e-9) - lo) / (hi - lo) * n)
        idx.append(k)
    return tuple(idx)

def treinar(episodios=5000, alfa=0.1, gamma=0.99, seed=0):
    rng = np.random.default_rng(seed)
    Q = np.zeros(bins + (2,))
    eps, retornos = 1.0, []
    for ep in range(episodios):
        obs, _ = env.reset(seed=int(rng.integers(1_000_000)))
        s, total, fim = discretizar(obs), 0, False
        while not fim:
            a = int(rng.integers(2)) if rng.random() < eps else int(Q[s].argmax())
            obs, r, term, trunc, _ = env.step(a)
            s2 = discretizar(obs)
            alvo = r + (0 if term else gamma * Q[s2].max())
            Q[s + (a,)] += alfa * (alvo - Q[s + (a,)])
            s, total, fim = s2, total + r, term or trunc
        retornos.append(total)
        eps = max(0.01, eps * 0.999)
    return Q, retornos

def avaliar(Q, n=100):
    totais = []
    for i in range(n):
        obs, _ = env.reset(seed=10_000 + i)
        total, fim = 0, False
        while not fim:
            obs, r, term, trunc, _ = env.step(int(Q[discretizar(obs)].argmax()))
            total, fim = total + r, term or trunc
        totais.append(total)
    return float(np.mean(totais))

if __name__ == "__main__":
    rng = np.random.default_rng(1)
    aleatorio = []
    for i in range(100):
        env.reset(seed=i)
        total, fim = 0, False
        while not fim:
            _, r, term, trunc, _ = env.step(int(rng.integers(2)))
            total, fim = total + r, term or trunc
        aleatorio.append(total)
    print("agente aleatorio, retorno medio:", round(float(np.mean(aleatorio)), 1))
    Q, retornos = treinar()
    print("Q-learning, retorno medio depois de treinar:", round(avaliar(Q), 1))
