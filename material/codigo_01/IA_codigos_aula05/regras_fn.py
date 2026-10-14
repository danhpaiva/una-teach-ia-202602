regras = [
    lambda f: f | {"molhado"} if "chuva" in f else f,
    lambda f: f | {"escorregadio"} if "molhado" in f else f,
]

fatos = frozenset({"chuva"})
for regra in regras:
    fatos = regra(fatos)
print(sorted(fatos))
