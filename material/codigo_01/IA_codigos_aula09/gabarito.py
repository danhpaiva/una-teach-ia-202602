from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# Exercicio 1: linha de base
base = DummyClassifier().fit(X_tr, y_tr)
print("ex1:", round(base.score(X_te, y_te), 3))

# Exercicio 2: escolher k
print("ex2:")
for k in [1, 5, 15]:
    m = KNeighborsClassifier(k).fit(X_tr, y_tr)
    print(" ", k, round(m.score(X_te, y_te), 3))

# Exercicio 3: profundidade da arvore (validacao cruzada, 5 dobras)
print("ex3:")
for d in [1, 2, 3, None]:
    arv = DecisionTreeClassifier(max_depth=d, random_state=0)
    print(" ", d, round(cross_val_score(arv, X, y, cv=5).mean(), 3))

# Exercicio 4: pipeline com escala + regressao logistica
pipe = make_pipeline(StandardScaler(),
    LogisticRegression(max_iter=1000))
print("ex4:", round(cross_val_score(pipe, X, y, cv=5).mean(), 3))
knn = make_pipeline(StandardScaler(), KNeighborsClassifier())
print("     k-NN para comparar:", round(cross_val_score(knn, X, y, cv=5).mean(), 3))
