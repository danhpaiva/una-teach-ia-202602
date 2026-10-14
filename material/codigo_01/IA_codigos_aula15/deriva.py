import numpy as np
from scipy.stats import ks_2samp
from sklearn.linear_model import LogisticRegression

rng = np.random.default_rng(0)

def gerar(n, media):
    X = rng.normal(media, 1, (n, 3))
    y = (X.sum(axis=1) > 3 * media + rng.normal(0, 1, n)).astype(int)
    return X, y

X_ant, y_ant = gerar(2000, media=0.0)          # dados da epoca do treino
X_novo, y_novo = gerar(2000, media=0.8)        # dados de hoje: o mundo mudou
modelo = LogisticRegression().fit(X_ant, y_ant)
print("acuracia nos dados antigos:", round(modelo.score(X_ant, y_ant), 3))
print("acuracia nos dados novos  :", round(modelo.score(X_novo, y_novo), 3))
for j in range(3):
    ks = ks_2samp(X_ant[:, j], X_novo[:, j])
    print(f"atributo {j}: estatistica KS = {ks.statistic:.3f}, p = {ks.pvalue:.1e}")
