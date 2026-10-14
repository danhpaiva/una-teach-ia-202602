from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for nome, m in [("arvore unica", DecisionTreeClassifier(random_state=42)),
                ("floresta 100", RandomForestClassifier(random_state=42))]:
    notas = cross_val_score(m, X, y, cv=cv)
    print(f"{nome:13} {notas.mean():.3f} +- {notas.std():.3f}")
