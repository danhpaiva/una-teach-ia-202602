from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

X, y = make_moons(n_samples=400, noise=0.15, random_state=0)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=0, stratify=y)

linear = LogisticRegression().fit(X_tr, y_tr)
rede = MLPClassifier(hidden_layer_sizes=(16, 16), max_iter=2000,
                     random_state=0).fit(X_tr, y_tr)
print("regressao logistica:", round(linear.score(X_te, y_te), 3))
print("rede neural        :", round(rede.score(X_te, y_te), 3))
