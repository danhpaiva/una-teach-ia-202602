from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

def nota(**kw):
    a = DecisionTreeClassifier(random_state=42, **kw)
    return cross_val_score(a, X, y, cv=cv).mean()

print("sem limite          :", round(nota(), 3))
print("max_depth=3         :", round(nota(max_depth=3), 3))
print("min_samples_leaf=10 :", round(nota(min_samples_leaf=10), 3))
print("ccp_alpha=0.01      :", round(nota(ccp_alpha=0.01), 3))
