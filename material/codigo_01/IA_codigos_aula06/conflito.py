regras = [
    ("A", {"febre"}, "suspeita_infeccao"),
    ("B", {"febre", "tosse", "dor_corpo"}, "suspeita_gripe"),
]
fatos = {"febre", "tosse", "dor_corpo"}
aplicaveis = [r for r in regras if r[1] <= fatos]
print([r[0] for r in aplicaveis])
escolhida = max(aplicaveis, key=lambda r: len(r[1]))
print(escolhida[0], escolhida[2])
