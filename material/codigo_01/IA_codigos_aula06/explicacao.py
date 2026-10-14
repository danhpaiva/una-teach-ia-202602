from frente import REGRAS

def provar(meta, fatos, regras, prova):
    if meta in fatos:
        return True
    for nome, premissas, conclusao in regras:
        if conclusao == meta:
            if all(provar(p, fatos, regras, prova)
                   for p in premissas):
                prova.append((nome, premissas, meta))
                return True
    return False

fatos = {"pc_nao_liga", "led_apagado", "tomada_ok", "cabo_ok"}
prova = []
if provar("trocar_fonte", fatos, REGRAS, prova):
    for nome, premissas, concl in prova:
        print(f"{nome}: {' e '.join(premissas)} => {concl}")
