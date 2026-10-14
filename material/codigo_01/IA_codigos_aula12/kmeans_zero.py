import numpy as np

def distancias(X, c):
    return np.linalg.norm(X[:, None, :] - c[None, :, :], axis=2)

def kmeans(X, k, iteracoes=100, seed=0):
    rng = np.random.default_rng(seed)
    c = X[rng.choice(len(X), k, replace=False)]
    for it in range(1, iteracoes + 1):
        rotulos = distancias(X, c).argmin(axis=1)
        novos = c.copy()
        for j in range(k):
            if np.any(rotulos == j):
                novos[j] = X[rotulos == j].mean(axis=0)
        if np.allclose(novos, c):
            break
        c = novos
    inercia = float((distancias(X, c).min(axis=1) ** 2).sum())
    return c, rotulos, inercia, it

if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    X, y = make_blobs(n_samples=300, centers=3, cluster_std=1.0,
                      random_state=42)
    for seed in range(5):
        c, rotulos, inercia, it = kmeans(X, 3, seed=seed)
        print("semente", seed, "inercia", round(inercia, 1),
              "iteracoes", it)
    c, rotulos, inercia, it = kmeans(X, 3, seed=2)
    print("centroides (semente 2):\n", np.round(c, 2))
    print("tamanhos:", np.bincount(rotulos).tolist())
