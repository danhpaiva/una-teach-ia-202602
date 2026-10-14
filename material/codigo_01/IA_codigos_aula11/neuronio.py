import numpy as np

def neuronio(x, w, b):
    z = np.dot(w, x) + b
    return 1 if z >= 0 else 0

w = np.array([1.0, 1.0])
entradas = [(0, 0), (0, 1), (1, 0), (1, 1)]
print("AND:", [neuronio(np.array(x), w, -1.5) for x in entradas])
print("OR :", [neuronio(np.array(x), w, -0.5) for x in entradas])
