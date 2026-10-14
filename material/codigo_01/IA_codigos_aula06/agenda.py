from frente import REGRAS

def regras_disparaveis(fatos, regras):
    return [r for r in regras
            if set(r[1]) <= fatos and r[2] not in fatos]

fatos = {"pc_nao_liga", "led_apagado", "tomada_ok", "cabo_ok"}
for nome, _, concl in regras_disparaveis(fatos, REGRAS):
    print(nome, concl)
fatos |= {"suspeita_energia"}
for nome, _, concl in regras_disparaveis(fatos, REGRAS):
    print(nome, concl)
