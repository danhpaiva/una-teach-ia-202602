from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

sem = KNeighborsClassifier()
com = make_pipeline(StandardScaler(), KNeighborsClassifier())
print("sem escala:", round(cross_val_score(sem, X, y, cv=cv).mean(), 3))
print("com escala:", round(cross_val_score(com, X, y, cv=cv).mean(), 3))
