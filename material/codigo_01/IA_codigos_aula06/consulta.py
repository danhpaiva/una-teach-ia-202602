from frente import REGRAS

PERGUNTAS = {
    "pc_nao_liga": "O computador nao liga?",
    "led_apagado": "O LED da fonte esta apagado?",
    "led_aceso": "O LED da fonte esta aceso?",
    "sem_video": "Nao aparece imagem no monitor?",
    "tomada_ok": "A tomada funciona (outro aparelho liga)?",
    "tomada_sem_energia": "A tomada esta sem energia?",
    "cabo_ok": "O cabo de forca esta bom?",
    "monitor_ok": "O monitor funciona em outro PC?",
}

def perguntar(fato, memoria):
    if fato not in memoria:
        r = input(PERGUNTAS[fato] + " (s/n) ").strip().lower()
        memoria[fato] = r.startswith("s")
    return memoria[fato]

def provar(meta, memoria):
    if meta in PERGUNTAS:
        return perguntar(meta, memoria)
    for nome, premissas, conclusao in REGRAS:
        if conclusao == meta:
            if all(provar(p, memoria) for p in premissas):
                print(f"  [{nome}] conclui: {meta}")
                return True
    return False

memoria = {}
for objetivo in ["trocar_fonte", "usar_outra_tomada",
                 "reencaixar_memoria"]:
    if provar(objetivo, memoria):
        print("DIAGNOSTICO:", objetivo)
        break
else:
    print("Nao consegui diagnosticar.")
