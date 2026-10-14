import numpy as np
from gridworld import GridWorld, ACOES

def escolher(Q, s, eps, rng):
    if rng.random() < eps:
        return int(rng.integers(4))
    return int(Q[s].argmax())

def treinar(episodios=500, alfa=0.1, gamma=0.9, eps0=1.0, eps_min=0.05,
            decaimento=0.99, max_passos=200, seed=0):
    rng = np.random.default_rng(seed)
    env = GridWorld()
    Q = np.zeros((16, 4))
    eps, retornos = eps0, []
    for ep in range(episodios):
        s, total, fim, passos = env.reset(), 0, False, 0
        while not fim and passos < max_passos:
            a = escolher(Q, s, eps, rng)
            s2, r, fim = env.step(a)
            alvo = r + (0 if fim else gamma * Q[s2].max())
            Q[s, a] += alfa * (alvo - Q[s, a])
            s, total, passos = s2, total + r, passos + 1
        retornos.append(total)
        eps = max(eps_min, eps * decaimento)
    return Q, retornos

if __name__ == "__main__":
    Q, retornos = treinar()
    setas = ["^", ">", "v", "<"]
    print("politica aprendida (T = armadilha, M = meta):")
    for l in range(4):
        linha = []
        for c in range(4):
            if (l, c) == (3, 3):
                linha.append("M")
            elif (l, c) == (1, 3):
                linha.append("T")
            else:
                linha.append(setas[int(Q[l * 4 + c].argmax())])
        print(" ".join(linha))
    print("Q do estado inicial:", np.round(Q[0], 2))
    print("primeiros 50 episodios:", round(float(np.mean(retornos[:50])), 2))
    print("ultimos 50 episodios  :", round(float(np.mean(retornos[-50:])), 2))
