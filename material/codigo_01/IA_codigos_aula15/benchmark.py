import time
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
lr = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
rede = make_pipeline(StandardScaler(),
                     MLPClassifier((16,), max_iter=2000, random_state=0))
modelos = {
    "Sempre a classe mais comum": DummyClassifier(strategy="most_frequent"),
    "Arvore (profundidade 3)": DecisionTreeClassifier(max_depth=3, random_state=0),
    "k-NN (k = 5)": make_pipeline(StandardScaler(), KNeighborsClassifier(5)),
    "Regressao logistica": lr,
    "Floresta aleatoria": RandomForestClassifier(n_estimators=200, random_state=0),
    "Rede neural (16)": rede,
}
for nome, modelo in modelos.items():
    t0 = time.perf_counter()
    acc = cross_val_score(modelo, X, y, cv=cv)
    seg = time.perf_counter() - t0
    print(f"{nome:27s} {acc.mean():.3f} +- {acc.std():.3f}   ({seg:.2f} s)")
