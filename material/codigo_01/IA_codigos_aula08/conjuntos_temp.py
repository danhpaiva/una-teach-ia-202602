import numpy as np
from pertinencia import tri, trap

def frio(t):
    return np.clip((20 - t) / 10, 0, 1)

def agradavel(t):
    return tri(t, 15, 22, 29)

def quente(t):
    return np.clip((t - 25) / 10, 0, 1)

for t in [10, 18, 22, 27, 33]:
    print(t, round(float(frio(t)), 2), round(float(agradavel(t)), 2),
          round(float(quente(t)), 2))
