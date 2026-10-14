import numpy as np

mapa = np.array([[1, 3, 2, 0],
                 [4, 8, 1, 1],
                 [0, 2, 7, 5],
                 [3, 1, 6, 9]])

def max_pooling(m, tamanho=2):
    n = m.shape[0] // tamanho
    saida = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            saida[i, j] = m[i * tamanho:(i + 1) * tamanho,
                            j * tamanho:(j + 1) * tamanho].max()
    return saida

print("mapa 4x4:\n", mapa)
print("max pooling 2x2:\n", max_pooling(mapa))
