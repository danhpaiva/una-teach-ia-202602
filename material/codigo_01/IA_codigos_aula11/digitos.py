from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

digitos = load_digits()
X = digitos.data / 16.0                 # pixels de 0 a 16 -> 0 a 1
y = digitos.target
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print(digitos.images.shape, X.shape)

rede = MLPClassifier(hidden_layer_sizes=(64,), max_iter=500, random_state=0)
rede.fit(X_tr, y_tr)
print("treino:", round(rede.score(X_tr, y_tr), 3))
print("teste :", round(rede.score(X_te, y_te), 3))
pred = rede.predict(X_te)
cm = confusion_matrix(y_te, pred)
erros = [(i, j, int(cm[i, j]))
         for i in range(10) for j in range(10)
         if i != j and cm[i, j]]
print("erros (real, previsto, quantos):", erros)
