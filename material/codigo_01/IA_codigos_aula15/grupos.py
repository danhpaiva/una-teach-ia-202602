import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)

def gerar(n, deslocamento):
    X = rng.normal(0, 1, (n, 2))
    y = (X[:, 0] + deslocamento * X[:, 1] > 0).astype(int)   # a regra muda com o grupo
    return X, y

Xa, ya = gerar(1800, 0.0)        # grupo A: 90% dos dados
Xb, yb = gerar(200, 3.0)         # grupo B: 10% dos dados, outra regra
X = np.vstack([Xa, Xb]); y = np.concatenate([ya, yb])
grupo = np.array(["A"] * 1800 + ["B"] * 200)

X_tr, X_te, y_tr, y_te, g_tr, g_te = train_test_split(
    X, y, grupo, test_size=0.3, random_state=0, stratify=grupo)
modelo = LogisticRegression().fit(X_tr, y_tr)
pred = modelo.predict(X_te)
print("acuracia geral:", round(float((pred == y_te).mean()), 3))
for g in ("A", "B"):
    m = g_te == g
    print("grupo", g, "| exemplos no teste:", int(m.sum()),
          "| acuracia:", round(float((pred[m] == y_te[m]).mean()), 3))
