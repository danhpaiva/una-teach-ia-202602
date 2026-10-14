from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

# 8 atributos: os 3 primeiros carregam informacao; os 5 ultimos sao ruido
X, y = make_classification(n_samples=1000, n_features=8, n_informative=3,
                           n_redundant=0, n_repeated=0, shuffle=False,
                           random_state=0)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0)
floresta = RandomForestClassifier(n_estimators=200, random_state=0).fit(X_tr, y_tr)
print("acuracia no teste:", round(floresta.score(X_te, y_te), 3))

r = permutation_importance(floresta, X_te, y_te, n_repeats=20, random_state=0)
for i in r.importances_mean.argsort()[::-1]:
    tipo = "informativo" if i < 3 else "ruido"
    print(f"atributo {i} ({tipo:11s}) queda media: {r.importances_mean[i]:.3f}")
