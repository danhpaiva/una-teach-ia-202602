import numpy as np

class Perceptron:
    def __init__(self, n_entradas, eta=0.1):
        self.w = np.zeros(n_entradas)
        self.b = 0.0
        self.eta = eta

    def prever(self, x):
        return 1 if np.dot(self.w, x) + self.b >= 0 else 0

    def treinar(self, X, y, epocas=20):
        for ep in range(1, epocas + 1):
            erros = 0
            for xi, yi in zip(X, y):
                erro = yi - self.prever(xi)
                if erro != 0:
                    self.w += self.eta * erro * xi
                    self.b += self.eta * erro
                    erros += 1
            if erros == 0:
                return ep
        return None

if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]],
                 dtype=float)
    for nome, y in [("AND", [0, 0, 0, 1]), ("OR", [0, 1, 1, 1]),
                    ("XOR", [0, 1, 1, 0])]:
        p = Perceptron(2)
        ep = p.treinar(X, np.array(y))
        previsoes = [p.prever(x) for x in X]
        print(nome, "convergiu:", ep, previsoes)
