from unify import unificar

fatos = [("pai", "joao", "maria"), ("pai", "joao", "pedro"),
         ("pai", "maria", "ana"), ("pai", "pedro", "lucas")]

def consultar(padrao, fatos, s=None):
    s = {} if s is None else s
    for f in fatos:
        r = unificar(padrao, f, s)
        if r is not None:
            yield r

def consultar_todas(metas, fatos, s=None):
    s = {} if s is None else s
    if not metas:
        yield s
        return
    for r in consultar(metas[0], fatos, s):
        yield from consultar_todas(metas[1:], fatos, r)

print(list(consultar(("pai", "joao", "Filho"), fatos)))
print(list(consultar(("pai", "Pai", "ana"), fatos)))
metas = [("pai", "X", "Y"), ("pai", "Y", "Z")]
for r in consultar_todas(metas, fatos):
    print(r["X"], "e avo de", r["Z"])
