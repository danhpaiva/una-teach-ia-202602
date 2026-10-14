import pandas as pd

df = pd.DataFrame({
    "aluno": ["Ana", "Bruno", "Carla", "Diego"],
    "horas": [2, 5, 8, 4],
    "nota": [5.0, 6.5, 9.0, 6.0],
})

print(df[df["nota"] >= 6])
df["aprovado"] = df["nota"] >= 6
print(df.groupby("aprovado")["horas"].mean())
