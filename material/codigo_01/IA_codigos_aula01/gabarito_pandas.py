# Gabarito do exercicio 3
import pandas as pd

produtos = pd.DataFrame({
    "nome": ["A", "B", "C"],
    "estoque": [4, 25, 9],
})
baixo = produtos["estoque"] < 10
print(produtos[baixo])
