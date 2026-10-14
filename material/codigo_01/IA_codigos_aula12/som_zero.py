import numpy as np

def treinar_som(X, linhas, colunas, epocas=2000, lr0=0.5, sigma0=3.0, seed=0):
    rng = np.random.default_rng(seed)
    W = rng.uniform(X.min(0), X.max(0), (linhas, colunas, X.shape[1]))
    ii, jj = np.meshgrid(np.arange(linhas), np.arange(colunas), indexing="ij")
    for t in range(epocas):
        frac = t / epocas
        lr = lr0 * (1 - frac)
        sigma = sigma0 * (1 - frac) + 0.5
        x = X[rng.integers(len(X))]
        d = np.linalg.norm(W - x, axis=2)
        bi, bj = np.unravel_index(d.argmin(), d.shape)
        dist2 = (ii - bi) ** 2 + (jj - bj) ** 2
        h = np.exp(-dist2 / (2 * sigma ** 2))
        W += lr * h[:, :, None] * (x - W)
    return W

def vencedor(W, x):
    d = np.linalg.norm(W - x, axis=2)
    return np.unravel_index(d.argmin(), d.shape)

def erro_quantizacao(W, X):
    return float(np.mean([np.linalg.norm(W[vencedor(W, x)] - x) for x in X]))

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import MinMaxScaler
    iris = load_iris()
    X = MinMaxScaler().fit_transform(iris.data)
    W0 = treinar_som(X, 6, 6, epocas=0)
    W = treinar_som(X, 6, 6, epocas=3000)
    print("erro de quantizacao antes :", round(erro_quantizacao(W0, X), 3))
    print("erro de quantizacao depois:", round(erro_quantizacao(W, X), 3))
    mapa = [["." for _ in range(6)] for _ in range(6)]
    votos = {}
    for x, y in zip(X, iris.target):
        votos.setdefault(vencedor(W, x), []).append(int(y))
    for (i, j), v in votos.items():
        mapa[i][j] = str(max(set(v), key=v.count))
    print("classe predominante em cada neuronio:")
    for linha in mapa:
        print(" ".join(linha))
