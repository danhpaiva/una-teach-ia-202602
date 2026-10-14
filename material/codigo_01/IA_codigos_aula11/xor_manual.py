import numpy as np

def degrau(z):
    return (z >= 0).astype(float)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)

# camada oculta: neuronio 1 = OR, neuronio 2 = NAND
W1 = np.array([[1.0, -1.0],
               [1.0, -1.0]])
b1 = np.array([-0.5, 1.5])
# saida = AND dos dois
W2 = np.array([[1.0], [1.0]])
b2 = np.array([-1.5])

oculta = degrau(X @ W1 + b1)
saida = degrau(oculta @ W2 + b2)
print("oculta:\n", oculta)
print("saida :", saida.ravel())
