from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target
a = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X, y)

caminho = a.decision_path(X[[0, 100]])
print(caminho.toarray())
folhas = a.apply(X[[0, 100]])
print("folhas:", folhas, "classes:", a.predict(X[[0, 100]]))
