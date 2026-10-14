REGRAS = [
    ("R1", ("pc_nao_liga", "led_apagado"), "suspeita_energia"),
    ("R2", ("suspeita_energia", "tomada_ok"), "suspeita_fonte"),
    ("R3", ("suspeita_fonte", "cabo_ok"), "trocar_fonte"),
    ("R4", ("suspeita_energia", "tomada_sem_energia"), "usar_outra_tomada"),
    ("R5", ("pc_nao_liga", "led_aceso", "sem_video"), "suspeita_video"),
    ("R6", ("suspeita_video", "monitor_ok"), "reencaixar_memoria"),
]

def encadeamento_frente(fatos, regras):
    fatos = set(fatos)
    rodada = 0
    while True:
        rodada += 1
        novos = {}
        for nome, premissas, conclusao in regras:
            if set(premissas) <= fatos and conclusao not in fatos:
                novos[conclusao] = nome
        if not novos:
            return fatos
        for conclusao, nome in novos.items():
            print(f"rodada {rodada}: {nome} => {conclusao}")
        fatos |= set(novos)

if __name__ == "__main__":
    inicial = {"pc_nao_liga", "led_apagado", "tomada_ok", "cabo_ok"}
    final = encadeamento_frente(inicial, REGRAS)
    print(sorted(final - inicial))
