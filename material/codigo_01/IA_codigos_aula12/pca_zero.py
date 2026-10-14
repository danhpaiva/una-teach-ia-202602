import numpy as np
from sklearn.datasets import load_iris

X = load_iris().data
Xc = X - X.mean(axis=0)                       # 1) centralizar
cov = np.cov(Xc, rowvar=False)                # 2) matriz de covariancia
valores, vetores = np.linalg.eigh(cov)        # 3) autovalores e autovetores
ordem = np.argsort(valores)[::-1]             # 4) do maior para o menor
valores, vetores = valores[ordem], vetores[:, ordem]
print("autovalores:", np.round(valores, 3))
print("variancia explicada:", np.round(valores / valores.sum(), 3))
Z = Xc @ vetores[:, :2]                       # 5) projetar em 2 componentes
print("forma de Z:", Z.shape)
print("primeira flor em 2D:", np.round(Z[0], 3))
