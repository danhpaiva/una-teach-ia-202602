import joblib
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# 1) Dados e divisao (o teste fica guardado ate o fim)
dados = load_breast_cancer()
X, y = dados.data, dados.target
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
print("treino:", X_tr.shape, " teste:", X_te.shape)

# 2) Linha de base: o minimo que qualquer modelo precisa superar
base = DummyClassifier(strategy="most_frequent").fit(X_tr, y_tr)
print("linha de base (classe mais comum):", round(base.score(X_te, y_te), 3))

# 3) Modelo candidato, avaliado so com validacao cruzada no treino
modelo = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
cv = cross_val_score(modelo, X_tr, y_tr, cv=5)
print("validacao cruzada:", round(cv.mean(), 3), "+-", round(cv.std(), 3))

# 4) Teste final, uma unica vez, e analise por classe
modelo.fit(X_tr, y_tr)
pred = modelo.predict(X_te)
print("acuracia no teste:", round(float((pred == y_te).mean()), 3))
print(confusion_matrix(y_te, pred))
print(classification_report(y_te, pred, target_names=dados.target_names, digits=3))

# 5) Salvar e reutilizar
joblib.dump(modelo, "modelo_final.joblib")
de_novo = joblib.load("modelo_final.joblib")
print("modelo recarregado reproduz o teste:", bool((de_novo.predict(X_te) == pred).all()))
