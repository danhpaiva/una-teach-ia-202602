import numpy as np
from grad2d import f, gradiente

p = np.array([3.0, 4.0])
alfa = 0.1
for passo in range(6):
    print(passo, p.round(3), round(f(p), 3))
    p = p - alfa * gradiente(f, p)
