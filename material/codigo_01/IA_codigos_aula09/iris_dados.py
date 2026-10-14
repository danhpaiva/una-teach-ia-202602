import pandas as pd
from sklearn.datasets import load_iris

pd.set_option("display.width", 100)
iris = load_iris(as_frame=True)
df = iris.frame
df.columns = ["sepala_c", "sepala_l", "petala_c", "petala_l", "alvo"]
df["especie"] = df["alvo"].map(dict(enumerate(iris.target_names)))

print(df.shape)
print(df.head(3))
print(df["especie"].value_counts())
print(df.groupby("especie")[["petala_c", "petala_l"]].mean().round(2))
