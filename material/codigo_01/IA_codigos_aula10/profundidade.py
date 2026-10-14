from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

for d in [1, 2, 3, 4, 5, 8, None]:
    a = DecisionTreeClassifier(max_depth=d, random_state=42).fit(X_tr, y_tr)
    print(f"max_depth={d!s:4} folhas={a.get_n_leaves():2}"
          f" treino={a.score(X_tr, y_tr):.3f} teste={a.score(X_te, y_te):.3f}")
