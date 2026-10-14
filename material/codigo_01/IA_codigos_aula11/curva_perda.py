from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)
esc = StandardScaler().fit(X_tr)
rede = MLPClassifier(hidden_layer_sizes=(16,), max_iter=500, random_state=0)
rede.fit(esc.transform(X_tr), y_tr)
perdas = rede.loss_curve_
print("iteracoes:", rede.n_iter_)
print([round(float(perdas[i]), 3) for i in (0, 9, 49, 99, len(perdas) - 1)])
print("teste:", round(rede.score(esc.transform(X_te), y_te), 3))
