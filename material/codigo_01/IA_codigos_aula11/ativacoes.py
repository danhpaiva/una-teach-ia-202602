import numpy as np

def degrau(z):
    return np.where(z >= 0, 1.0, 0.0)

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return np.tanh(z)

def relu(z):
    return np.maximum(0, z)

z = np.array([-2.0, -0.5, 0.0, 0.5, 2.0])
for f in (degrau, sigmoide, tanh, relu):
    print(f"{f.__name__:9}", np.round(f(z), 3))
