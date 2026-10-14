import numpy as np

def sig(z):
    return 1 / (1 + np.exp(-z))

x = np.array([1.0, 0.0])
y = 1.0
W1 = np.array([[0.5, -0.4], [0.3, 0.8]])   # linha = entrada, coluna = neuronio oculto
b1 = np.array([0.1, -0.2])
W2 = np.array([0.7, -0.6])
b2 = 0.05

def perda(W1, b1, W2, b2):
    a1 = sig(x @ W1 + b1)
    a2 = sig(a1 @ W2 + b2)
    return 0.5 * (a2 - y) ** 2

# forward
z1 = x @ W1 + b1
a1 = sig(z1)
z2 = a1 @ W2 + b2
a2 = sig(z2)
print("z1 =", np.round(z1, 4))
print("a1 =", np.round(a1, 4))
print("z2 =", round(z2, 4), " a2 =", round(a2, 4))
print("perda =", round(perda(W1, b1, W2, b2), 5))

# backward (regra da cadeia)
d2 = (a2 - y) * a2 * (1 - a2)                 # dL/dz2
gW2 = d2 * a1
gb2 = d2
d1 = d2 * W2 * a1 * (1 - a1)                  # dL/dz1
gW1 = np.outer(x, d1)
gb1 = d1
print("d2 =", round(d2, 5))
print("gW2 =", np.round(gW2, 5))
print("d1 =", np.round(d1, 5))

# verificacao numerica (diferenca central, aula 03)
h = 1e-6
W2p, W2m = W2.copy(), W2.copy()
W2p[0] += h; W2m[0] -= h
num = (perda(W1, b1, W2p, b2) - perda(W1, b1, W2m, b2)) / (2 * h)
print("dL/dW2[0]: analitico =", round(gW2[0], 6), " numerico =", round(num, 6))
W1p, W1m = W1.copy(), W1.copy()
W1p[0, 0] += h; W1m[0, 0] -= h
num = (perda(W1p, b1, W2, b2) - perda(W1m, b1, W2, b2)) / (2 * h)
print("dL/dW1[0,0]: analitico =", round(gW1[0, 0], 6), " numerico =", round(num, 6))

# um passo de descida do gradiente
alfa = 1.0
nova = perda(W1 - alfa * gW1, b1 - alfa * gb1, W2 - alfa * gW2, b2 - alfa * gb2)
print("perda antes:", round(perda(W1, b1, W2, b2), 5),
      " depois:", round(nova, 5))
