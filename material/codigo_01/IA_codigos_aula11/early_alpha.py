from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

def nota(**kw):
    m = make_pipeline(StandardScaler(),
        MLPClassifier(hidden_layer_sizes=(64, 64), max_iter=2000,
                      random_state=0, **kw))
    return cross_val_score(m, X, y, cv=cv).mean()

print("padrao (alpha=0.0001):", round(nota(), 3))
print("alpha=1.0            :", round(nota(alpha=1.0), 3))
print("early_stopping=True  :", round(nota(early_stopping=True), 3))
