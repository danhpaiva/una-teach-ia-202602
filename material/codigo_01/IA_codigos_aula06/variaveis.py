from unify import unificar

REGRAS = [
    ([("pai", "X", "Y")], ("ancestral", "X", "Y")),
    ([("pai", "X", "Y"), ("ancestral", "Y", "Z")],
     ("ancestral", "X", "Z")),
]
FATOS = {("pai", "joao", "maria"), ("pai", "maria", "ana"),
         ("pai", "ana", "bia")}

def casar(premissas, fatos, s):
    if not premissas:
        yield s
        return
    for f in list(fatos):
        r = unificar(premissas[0], f, s)
        if r is not None:
            yield from casar(premissas[1:], fatos, r)

def aplicar(t, s):
    return tuple(s.get(x, x) for x in t)

def frente(regras, fatos):
    fatos = set(fatos)
    while True:
        novos = set()
        for premissas, conclusao in regras:
            for s in casar(premissas, fatos, {}):
                f = aplicar(conclusao, s)
                if f not in fatos:
                    novos.add(f)
        if not novos:
            return fatos
        fatos |= novos

for f in sorted(frente(REGRAS, FATOS)):
    if f[0] == "ancestral":
        print(f)
