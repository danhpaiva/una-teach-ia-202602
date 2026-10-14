import numpy as np
from pertinencia import tri

x = np.linspace(0, 25, 251)
agregada = np.maximum(np.minimum(0.4, tri(x, 0, 0, 13)),
                      np.minimum(0.8, tri(x, 13, 25, 25)))

centroide = (x * agregada).sum() / agregada.sum()
maximos = x[agregada == agregada.max()]
print("centroide    :", round(centroide, 2))
print("media maximos:", round(maximos.mean(), 2))
print("primeiro max :", round(maximos.min(), 2))
print("ultimo max   :", round(maximos.max(), 2))
