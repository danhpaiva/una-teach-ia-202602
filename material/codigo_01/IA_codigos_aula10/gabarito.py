from sklearn.datasets import load_wine
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

from dados_tenis import DADOS, ATRIBUTOS
from entropia import entropia, gini, ganho
from id3 import id3, prever

# Exercicio 1: impureza
print("ex1:", entropia(["a"] * 14), entropia(["a"] * 7 + ["b"] * 7),
      gini(["a"] * 7 + ["b"] * 7))

# Exercicio 2: ganho dentro do ramo "ensolarado"
sol = [d for d in DADOS if d[0] == "ensolarado"]
print("ex2:")
for i in (1, 2, 3):
    print(" ", ATRIBUTOS[i], round(ganho(sol, i), 3))

# Exercicio 3: arvores no conjunto wine
X, y = load_wine(return_X_y=True)
print("ex3:")
for d in [1, 2, 3, None]:
    a = DecisionTreeClassifier(max_depth=d, random_state=0)
    print(" ", d, round(cross_val_score(a, X, y, cv=5).mean(), 3))

# Exercicio 4: previsao com a arvore ID3
arvore = id3(DADOS, ATRIBUTOS)
novo = {"tempo": "chuvoso", "temperatura": "ameno",
        "umidade": "normal", "vento": "forte"}
print("ex4:", prever(arvore, novo))
