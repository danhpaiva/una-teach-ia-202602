import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = x ** 2

plt.plot(x, y, label="custo = x²")
plt.xlabel("parâmetro")
plt.ylabel("custo")
plt.legend()
plt.show()
