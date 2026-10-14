import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier

dados = load_breast_cancer()
X, y = dados.data, dados.target
rng = np.random.default_rng(0)

for rodada in range(6):
    idx = rng.choice(len(X), size=int(0.8 * len(X)), replace=False)
    a = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X[idx], y[idx])
    raiz = dados.feature_names[a.tree_.feature[0]]
    limiar = a.tree_.threshold[0]
    print(f"rodada {rodada}: raiz = {raiz} <= {limiar:.2f}")
