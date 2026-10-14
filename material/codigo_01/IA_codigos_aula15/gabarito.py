"""Gabarito da Aula 15 - exercicios 1 a 4 (autocontido)."""
from collections import Counter, defaultdict

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

print("Exercicio 1 (acrescentar Naive Bayes ao benchmark)")
X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
lr = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
for nome, modelo in (("Naive Bayes", GaussianNB()), ("Regressao logistica", lr)):
    acc = cross_val_score(modelo, X, y, cv=cv)
    print(f"{nome:20s} {acc.mean():.3f} +- {acc.std():.3f}")

print("\nExercicio 2 (modelo de bigramas)")
texto = ("o gato dorme no sofa . o gato come o peixe . o cao dorme no tapete . "
         "o cao come a carne . a menina le o livro . a menina come o peixe . "
         "o cao le o jornal . o gato dorme no tapete .")
palavras = texto.split()
contagem = defaultdict(Counter)
for atual, proxima in zip(palavras, palavras[1:]):
    contagem[atual][proxima] += 1
total = sum(contagem["a"].values())
for w, c in contagem["a"].most_common():
    print("depois de 'a':", w, round(c / total, 2))

print("\nExercicio 3 (quanto o mundo mudou)")
rng = np.random.default_rng(0)


def gerar(n, media):
    X = rng.normal(media, 1, (n, 3))
    y = (X.sum(axis=1) > 3 * media + rng.normal(0, 1, n)).astype(int)
    return X, y


X_ant, y_ant = gerar(2000, media=0.0)
modelo = LogisticRegression().fit(X_ant, y_ant)
for media in (0.0, 0.2, 0.4, 0.8):
    X_novo, y_novo = gerar(2000, media=media)
    acc = modelo.score(X_novo, y_novo)
    print("media dos dados novos:", media, "| acuracia:", round(acc, 3))

print("\nExercicio 4 (modelo so para o grupo B)")
rng = np.random.default_rng(0)


def gerar_grupo(n, deslocamento):
    X = rng.normal(0, 1, (n, 2))
    return X, (X[:, 0] + deslocamento * X[:, 1] > 0).astype(int)


Xa, ya = gerar_grupo(1800, 0.0)
Xb, yb = gerar_grupo(200, 3.0)
X = np.vstack([Xa, Xb])
y = np.concatenate([ya, yb])
grupo = np.array(["A"] * 1800 + ["B"] * 200)
X_tr, X_te, y_tr, y_te, g_tr, g_te = train_test_split(
    X, y, grupo, test_size=0.3, random_state=0, stratify=grupo)
geral = LogisticRegression().fit(X_tr, y_tr)
so_b = LogisticRegression().fit(X_tr[g_tr == "B"], y_tr[g_tr == "B"])
mb = g_te == "B"
print("grupo B, modelo geral :", round(geral.score(X_te[mb], y_te[mb]), 3))
print("grupo B, modelo so de B:", round(so_b.score(X_te[mb], y_te[mb]), 3))
