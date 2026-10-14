from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)
print(X_tr.shape, X_te.shape)

modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_tr, y_tr)
print("acuracia treino:", round(modelo.score(X_tr, y_tr), 3))
print("acuracia teste :", round(modelo.score(X_te, y_te), 3))
print(modelo.predict(X_te[:5]), y_te[:5])
