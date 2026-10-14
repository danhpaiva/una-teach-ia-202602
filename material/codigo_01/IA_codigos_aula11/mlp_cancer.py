from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

sem = MLPClassifier(hidden_layer_sizes=(16,), max_iter=2000, random_state=0)
com = make_pipeline(StandardScaler(),
                    MLPClassifier(hidden_layer_sizes=(16,), max_iter=2000,
                                  random_state=0))
print("sem escala:", round(cross_val_score(sem, X, y, cv=cv).mean(), 3))
print("com escala:", round(cross_val_score(com, X, y, cv=cv).mean(), 3))
