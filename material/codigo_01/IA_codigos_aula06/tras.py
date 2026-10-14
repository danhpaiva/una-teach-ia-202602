from frente import REGRAS

def provar(meta, fatos, regras, nivel=0):
    recuo = "  " * nivel
    if meta in fatos:
        print(f"{recuo}{meta}: fato conhecido")
        return True
    for nome, premissas, conclusao in regras:
        if conclusao == meta:
            print(f"{recuo}{meta}: tentando {nome}")
            if all(provar(p, fatos, regras, nivel + 1)
                   for p in premissas):
                return True
    print(f"{recuo}{meta}: nao provado")
    return False

if __name__ == "__main__":
    fatos = {"pc_nao_liga", "led_apagado", "tomada_ok", "cabo_ok"}
    print(provar("trocar_fonte", fatos, REGRAS))
    print(provar("reencaixar_memoria", fatos, REGRAS))
