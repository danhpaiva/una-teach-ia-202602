from frente import REGRAS, encadeamento_frente
from tras import provar
from unify import unificar

# Exercicio 1: nova regra R7
R7 = ("R7", ("pc_nao_liga", "led_aceso", "bipes"), "suspeita_memoria")
fatos = {"pc_nao_liga", "led_aceso", "bipes"}
print("ex1:")
encadeamento_frente(fatos, REGRAS + [R7])

# Exercicio 2: provar usar_outra_tomada
print("ex2:")
fatos2 = {"pc_nao_liga", "led_apagado", "tomada_sem_energia"}
print(provar("usar_outra_tomada", fatos2, REGRAS))

# Exercicio 3: fatores de certeza (modelo simplificado do MYCIN)
def combinar(cf1, cf2):
    return cf1 + cf2 * (1 - cf1)

print("ex3:", combinar(0.7, 0.5))                         # 0.85

# Exercicio 4: regra com variaveis, avo(X, Z) <- pai(X, Y) E pai(Y, Z)
REGRAS_V = [
    ([("pai", "X", "Y")], ("ancestral", "X", "Y")),
    ([("pai", "X", "Y"), ("ancestral", "Y", "Z")], ("ancestral", "X", "Z")),
]
FATOS_V = {("pai", "joao", "maria"), ("pai", "maria", "ana"),
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

REGRAS_V.append(([("pai", "X", "Y"), ("pai", "Y", "Z")], ("avo", "X", "Z")))
print("ex4:", sorted(f for f in frente(REGRAS_V, FATOS_V) if f[0] == "avo"))
