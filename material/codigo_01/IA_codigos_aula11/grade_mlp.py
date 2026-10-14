from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV, train_test_split, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)
pipe = make_pipeline(StandardScaler(), MLPClassifier(max_iter=2000, random_state=0))
grade = {"mlpclassifier__hidden_layer_sizes": [(4,), (16,), (64,), (16, 16)],
         "mlpclassifier__activation": ["relu", "tanh"]}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
busca = GridSearchCV(pipe, grade, cv=cv).fit(X_tr, y_tr)
print("melhores:", busca.best_params_)
print("cv      :", round(busca.best_score_, 3))
print("teste   :", round(busca.score(X_te, y_te), 3))
