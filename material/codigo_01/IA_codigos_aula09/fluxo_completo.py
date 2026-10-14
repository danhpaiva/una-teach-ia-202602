from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 1) dados   2) separar o teste e NAO olhar ate o fim
X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 3) modelo + pre-processamento juntos
modelo = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))

# 4) validacao cruzada so no treino
print("cv:", cross_val_score(modelo, X_tr, y_tr, cv=5).mean().round(3))

# 5) treino final e UMA avaliacao no teste
modelo.fit(X_tr, y_tr)
print("teste:", round(modelo.score(X_te, y_te), 3))
