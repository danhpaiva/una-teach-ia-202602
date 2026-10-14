from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier

dados = load_breast_cancer()
a = DecisionTreeClassifier(max_depth=3, random_state=42).fit(dados.data, dados.target)
pares = sorted(zip(a.feature_importances_, dados.feature_names), reverse=True)
for imp, nome in pares[:4]:
    print(f"{nome:25} {imp:.3f}")
