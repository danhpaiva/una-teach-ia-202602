# erro (graus acima do alvo) -> potencia, tabela consultada por interpolacao
import numpy as np
from ar_condicionado import potencia

for e in np.arange(-4, 9, 2):
    print(f"{e:+.0f}: {potencia(float(e)):5.1f}")
