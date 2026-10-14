import numpy as np

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

def iniciar(n_in, n_oc, seed=0, zeros=False):
    rng = np.random.default_rng(seed)
    if zeros:
        return {"W1": np.zeros((n_in, n_oc)), "b1": np.zeros(n_oc),
                "W2": np.zeros((n_oc, 1)), "b2": np.zeros(1)}
    return {"W1": rng.normal(0, 1, (n_in, n_oc)), "b1": np.zeros(n_oc),
            "W2": rng.normal(0, 1, (n_oc, 1)), "b2": np.zeros(1)}

def forward(p, X):
    a1 = sigmoide(X @ p["W1"] + p["b1"])
    a2 = sigmoide(a1 @ p["W2"] + p["b2"])
    return a1, a2

def perda(y, a2):
    eps = 1e-9
    return -np.mean(y * np.log(a2 + eps) + (1 - y) * np.log(1 - a2 + eps))

def backward(p, X, y, a1, a2):
    n = len(X)
    d2 = (a2 - y) / n                          # erro na saida
    g = {"W2": a1.T @ d2, "b2": d2.sum(axis=0)}
    d1 = (d2 @ p["W2"].T) * a1 * (1 - a1)
    g["W1"] = X.T @ d1
    g["b1"] = d1.sum(axis=0)
    return g

def treinar(X, y, n_oc=4, alfa=1.0, epocas=5000, seed=0, zeros=False):
    p = iniciar(X.shape[1], n_oc, seed, zeros)
    historico = []
    for ep in range(epocas):
        a1, a2 = forward(p, X)
        historico.append(perda(y, a2))
        g = backward(p, X, y, a1, a2)
        for k in p:
            p[k] -= alfa * g[k]
    return p, historico

if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([[0], [1], [1], [0]], dtype=float)
    p, h = treinar(X, y)
    _, saida = forward(p, X)
    print("perda:", [round(float(h[i]), 4) for i in (0, 100, 500, 1000, 4999)])
    print("saidas:", np.round(saida.ravel(), 3))
