import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
x = np.sort(rng.uniform(0, 10, 200)).reshape(-1, 1)
y = np.sin(x).ravel() + rng.normal(0, 0.15, 200)
x_tr, y_tr = x[::2], y[::2]
x_te, y_te = x[1::2], y[1::2]

rede = make_pipeline(StandardScaler(),
    MLPRegressor(hidden_layer_sizes=(32, 32), activation="tanh",
                 max_iter=5000, random_state=0))
rede.fit(x_tr, y_tr)
reta = LinearRegression().fit(x_tr, y_tr)
print("R2 teste, rede:", round(rede.score(x_te, y_te), 3))
print("R2 teste, reta:", round(reta.score(x_te, y_te), 3))
