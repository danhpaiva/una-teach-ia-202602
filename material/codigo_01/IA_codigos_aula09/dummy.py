import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score

y = np.array([0] * 950 + [1] * 50)       # 5% de fraudes
X = np.zeros((1000, 1))

ingenuo = DummyClassifier(strategy="most_frequent").fit(X, y)
pred = ingenuo.predict(X)
print("acuracia:", accuracy_score(y, pred))
print("recall da classe fraude:", recall_score(y, pred))
