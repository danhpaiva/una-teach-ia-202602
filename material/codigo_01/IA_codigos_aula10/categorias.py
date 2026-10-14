import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from dados_tenis import DADOS, ATRIBUTOS

df = pd.DataFrame(DADOS, columns=ATRIBUTOS + ["jogar"])
X = pd.get_dummies(df[ATRIBUTOS])          # uma coluna 0/1 por categoria
y = df["jogar"]
a = DecisionTreeClassifier(random_state=0).fit(X, y)
print(list(X.columns)[:5], "...", X.shape)
print("treino:", a.score(X, y))
