from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

iris = load_iris()
X_tr, X_te, y_tr, y_te = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42, stratify=iris.target)

arvore = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_tr, y_tr)
print("treino:", round(arvore.score(X_tr, y_tr), 3))
print("teste :", round(arvore.score(X_te, y_te), 3))
nomes = ["sepala_c", "sepala_l", "petala_c", "petala_l"]
print(export_text(arvore, feature_names=nomes))
