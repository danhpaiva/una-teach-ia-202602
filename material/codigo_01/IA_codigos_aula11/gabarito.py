"""Gabarito da Aula 11 - exercicios 1 a 4 (autocontido)."""
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def neuronio(x, w, b):
    z = np.dot(w, x) + b
    return 1 if z >= 0 else 0


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


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)

print("Exercicio 1 (NAND com um neuronio)")
w = np.array([-1.0, -1.0]);  b = 1.5
for x in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(x, neuronio(np.array(x), w, b))

print("\nExercicio 2 (parametros)")
def n_param(camadas):
    return sum(a * b + b for a, b in zip(camadas[:-1], camadas[1:]))
print("4-8-3:", n_param([4, 8, 3]))
print("64-64-10:", n_param([64, 64, 10]))

print("\nExercicio 3 (perceptron em NAND e XOR)")
y = np.array([1, 1, 1, 0])
p = Perceptron(2)
print("NAND converge na epoca", p.treinar(X, y))
p = Perceptron(2)
print("XOR:", p.treinar(X, np.array([0, 1, 1, 0])))

print("\nExercicio 4 (MLP nos digitos)")
digitos = load_digits()
Xd = digitos.data / 16.0
X_tr, X_te, y_tr, y_te = train_test_split(
    Xd, digitos.target, test_size=0.25, random_state=42,
    stratify=digitos.target)
for h in (32, 128):
    r = MLPClassifier(hidden_layer_sizes=(h,), max_iter=500,
                      random_state=0)
    r.fit(X_tr, y_tr)
    print(h, round(r.score(X_te, y_te), 3))
