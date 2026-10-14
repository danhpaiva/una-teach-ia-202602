import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X, y = load_diabetes(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression().fit(X_tr, y_tr)
pred = modelo.predict(X_te)

print("MAE :", round(mean_absolute_error(y_te, pred), 1))
print("RMSE:", round(np.sqrt(mean_squared_error(y_te, pred)), 1))
print("R2  :", round(r2_score(y_te, pred), 3))
print("media simples (referencia) MAE:", round(mean_absolute_error(y_te, np.full_like(y_te, y_tr.mean(), dtype=float)), 1))
for real, prev in list(zip(y_te, pred))[:4]:
    print(int(real), round(prev))
