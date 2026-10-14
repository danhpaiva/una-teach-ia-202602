# Gabarito do exercicio 4
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)

plt.plot(x, 2 * x + 1, label="2x+1")
plt.plot(x, x ** 2, label="x²")
plt.legend()
plt.show()
