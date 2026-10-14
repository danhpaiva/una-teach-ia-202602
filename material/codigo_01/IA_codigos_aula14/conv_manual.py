import numpy as np

imagem = np.array([[0, 0, 0, 9, 9, 9],
                   [0, 0, 0, 9, 9, 9],
                   [0, 0, 0, 9, 9, 9],
                   [0, 0, 0, 9, 9, 9],
                   [0, 0, 0, 9, 9, 9],
                   [0, 0, 0, 9, 9, 9]])
filtro = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])           # detector de borda vertical

def convolucao(img, f):
    n = f.shape[0]
    saida = np.zeros((img.shape[0] - n + 1, img.shape[1] - n + 1))
    for i in range(saida.shape[0]):
        for j in range(saida.shape[1]):
            trecho = img[i:i + n, j:j + n]
            saida[i, j] = np.sum(trecho * f)
    return saida

if __name__ == "__main__":
    mapa = convolucao(imagem, filtro)
    print("forma da saida:", mapa.shape)
    print(mapa.astype(int))
    print("primeiro trecho 3x3:\n", imagem[0:3, 0:3])
    print("soma dos produtos nele:", int(np.sum(imagem[0:3, 0:3] * filtro)))
    print("trecho sobre a borda:\n", imagem[0:3, 1:4])
    print("soma dos produtos nele:", int(np.sum(imagem[0:3, 1:4] * filtro)))
