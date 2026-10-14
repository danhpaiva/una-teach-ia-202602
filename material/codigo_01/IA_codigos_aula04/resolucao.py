from itertools import combinations

def negar(l):
    return l[1:] if l.startswith("~") else "~" + l

def resolver(c1, c2):
    resultados = []
    for l in c1:
        if negar(l) in c2:
            novo = (c1 - {l}) | (c2 - {negar(l)})
            resultados.append(frozenset(novo))
    return resultados

def resolucao(clausulas, consulta):
    clausulas = set(clausulas)
    clausulas.add(frozenset({negar(consulta)}))
    while True:
        novas = set()
        for c1, c2 in combinations(list(clausulas), 2):
            for r in resolver(c1, c2):
                if not r:
                    return True
                novas.add(r)
        if novas <= clausulas:
            return False
        clausulas |= novas

KB = [frozenset({"p", "q"}), frozenset({"~p", "r"}), frozenset({"~q", "r"})]
print(resolucao(KB, "r"))
print(resolucao(KB, "~r"))
print(resolucao(KB, "p"))
