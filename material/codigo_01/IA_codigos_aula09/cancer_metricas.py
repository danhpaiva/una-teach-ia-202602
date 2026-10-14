from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

dados = load_breast_cancer()
X, y = dados.data, dados.target       # 0 = maligno, 1 = benigno
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

modelo = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
modelo.fit(X_tr, y_tr)
pred = modelo.predict(X_te)
print(confusion_matrix(y_te, pred))
print(classification_report(y_te, pred, target_names=dados.target_names, digits=3))
