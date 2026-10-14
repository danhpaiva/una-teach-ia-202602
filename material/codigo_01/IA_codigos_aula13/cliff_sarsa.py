import gymnasium as gym
import numpy as np

def epsilon_gulosa(Q, s, eps, rng):
    if rng.random() < eps:
        return int(rng.integers(4))
    return int(Q[s].argmax())

def treinar(metodo, episodios=500, alfa=0.5, gamma=1.0, eps=0.1, seed=0):
    env = gym.make("CliffWalking-v1")
    rng = np.random.default_rng(seed)
    Q = np.zeros((48, 4))
    retornos = []
    for ep in range(episodios):
        s, _ = env.reset(seed=int(rng.integers(1_000_000)))
        a = epsilon_gulosa(Q, s, eps, rng)
        total, fim = 0, False
        while not fim:
            s2, r, term, trunc, _ = env.step(a)
            a2 = epsilon_gulosa(Q, s2, eps, rng)
            if metodo == "q-learning":
                proximo = Q[s2].max()
            else:                                  # SARSA
                proximo = Q[s2, a2]
            Q[s, a] += alfa * (r + (0 if term else gamma * proximo) - Q[s, a])
            s, a, total, fim = s2, a2, total + r, term or trunc
        retornos.append(total)
    return Q, retornos

def retorno_guloso(Q):
    env = gym.make("CliffWalking-v1")
    s, _ = env.reset(seed=0)
    total, fim, passos = 0, False, 0
    while not fim and passos < 100:
        s, r, term, trunc, _ = env.step(int(Q[s].argmax()))
        total, fim, passos = total + r, term or trunc, passos + 1
    return total

if __name__ == "__main__":
    for metodo in ("q-learning", "sarsa"):
        treino, guloso = [], []
        for seed in range(10):
            Q, ret = treinar(metodo, seed=seed)
            treino.append(np.mean(ret[-100:]))
            guloso.append(retorno_guloso(Q))
        print(metodo, "| retorno durante o treino:", round(float(np.mean(treino)), 1),
              "| mediana da politica gulosa:", int(np.median(guloso)))
