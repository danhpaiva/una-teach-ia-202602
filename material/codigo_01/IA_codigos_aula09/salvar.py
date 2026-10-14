import joblib
from sklearn.datasets import load_iris
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
modelo = make_pipeline(StandardScaler(), KNeighborsClassifier()).fit(X, y)
joblib.dump(modelo, "modelo_iris.joblib")

carregado = joblib.load("modelo_iris.joblib")
print(carregado.predict([[5.1, 3.5, 1.4, 0.2], [6.7, 3.0, 5.2, 2.3]]))
