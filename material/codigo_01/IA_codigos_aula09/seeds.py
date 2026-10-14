from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
for seed in range(6):
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.3, random_state=seed, stratify=y)
    modelo = KNeighborsClassifier().fit(X_tr, y_tr)
    print(f"random_state={seed}: {modelo.score(X_te, y_te):.3f}")
