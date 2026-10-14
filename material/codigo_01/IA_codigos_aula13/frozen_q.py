import gymnasium as gym
import numpy as np

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

if __name__ == "__main__":
    for escorregadio in (False, True):
        env = gym.make("FrozenLake-v1", is_slippery=escorregadio)
        Q = treinar(env, 5000)
        print("is_slippery =", escorregadio, "-> sucesso da politica gulosa:",
              taxa_sucesso(env, Q))
