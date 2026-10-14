from itertools import product

def implica(p, q):
    return (not p) or q

print("p      q      E      OU     ->")
for p, q in product([True, False], repeat=2):
    linha = [p, q, p and q, p or q, implica(p, q)]
    print(*[str(v).ljust(7) for v in linha], sep="")
