import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(1)
grupos = [(24, 2500, 70, 100), (45, 9000, 30, 100), (38, 5000, 55, 100)]
linhas = []
for idade, renda, gasto, n in grupos:
    linhas.append(np.column_stack([
        rng.normal(idade, 4, n), rng.normal(renda, 600, n),
        rng.normal(gasto, 8, n)]))
df = pd.DataFrame(np.vstack(linhas), columns=["idade", "renda", "gasto"])

modelo = make_pipeline(StandardScaler(),
                       KMeans(n_clusters=3, n_init=10, random_state=0))
df["segmento"] = modelo.fit_predict(df)
Xe = StandardScaler().fit_transform(df[["idade", "renda", "gasto"]])
print("silhueta:", round(silhouette_score(Xe, df["segmento"]), 3))
print(df.groupby("segmento").agg(clientes=("idade", "size"),
      idade=("idade", "mean"), renda=("renda", "mean"),
      gasto=("gasto", "mean")).round(1))
