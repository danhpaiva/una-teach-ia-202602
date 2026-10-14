from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

modelos = {
    "Regressao logistica": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "k-NN (k=5)": make_pipeline(StandardScaler(), KNeighborsClassifier()),
    "Arvore de decisao": DecisionTreeClassifier(random_state=42),
    "Floresta aleatoria": RandomForestClassifier(random_state=42),
}
for nome, m in modelos.items():
    notas = cross_val_score(m, X, y, cv=cv)
    print(f"{nome:20} {notas.mean():.3f} +- {notas.std():.3f}")
