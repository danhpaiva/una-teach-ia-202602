import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(0)
x = np.sort(rng.uniform(0, 10, 80)).reshape(-1, 1)
y = np.sin(x).ravel() + rng.normal(0, 0.2, 80)

arv = DecisionTreeRegressor(max_depth=3).fit(x, y)
reta = LinearRegression().fit(x, y)
print("arvore R2:", round(arv.score(x, y), 3), "folhas:", arv.get_n_leaves())
print("reta   R2:", round(reta.score(x, y), 3))
print(np.round(arv.predict([[1.0], [3.0], [5.0], [8.0]]), 2))
