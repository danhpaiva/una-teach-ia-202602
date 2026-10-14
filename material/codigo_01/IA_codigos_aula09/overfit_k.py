from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = make_moons(n_samples=300, noise=0.35, random_state=0)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=0, stratify=y)

for k in [1, 3, 5, 9, 15, 25, 51, 101]:
    m = KNeighborsClassifier(n_neighbors=k).fit(X_tr, y_tr)
    print(f"k={k:3}  treino={m.score(X_tr, y_tr):.3f}  teste={m.score(X_te, y_te):.3f}")
