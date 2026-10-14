import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

rng = np.random.default_rng(0)
X = rng.normal(size=(100, 2000))          # ruido puro
y = rng.integers(0, 2, size=100)          # rotulos aleatorios
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

# ERRADO: seleciona as melhores colunas usando TODOS os dados
X_sel = SelectKBest(f_classif, k=20).fit_transform(X, y)
errado = cross_val_score(LogisticRegression(max_iter=1000), X_sel, y, cv=cv).mean()

# CERTO: selecao dentro do pipeline (so ve o treino de cada dobra)
pipe = make_pipeline(SelectKBest(f_classif, k=20), LogisticRegression(max_iter=1000))
certo = cross_val_score(pipe, X, y, cv=cv).mean()
print("com vazamento:", round(errado, 3))
print("sem vazamento:", round(certo, 3))
