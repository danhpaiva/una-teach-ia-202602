from ar_condicionado import potencia

ALVO, T_EXT = 24.0, 35.0

def simular(controle, T0=32.0, passos=120):
    T, hist, energia = T0, [], 0.0
    for _ in range(passos):
        p = controle(T - ALVO)
        T += 0.04 * (T_EXT - T) - 0.012 * p
        hist.append(T)
        energia += p / 100
    return hist, energia

def termostato(erro):
    if erro > 0.5:
        termostato.ligado = True
    elif erro < -0.5:
        termostato.ligado = False
    return 100.0 if termostato.ligado else 0.0
termostato.ligado = False

def oscilacao(hist):
    estavel = hist[60:]
    return max(estavel) - min(estavel)

hf, ef = simular(potencia)
ht, et = simular(termostato)
print(f"fuzzy    : final {hf[-1]:.2f}  oscilacao {oscilacao(hf):.2f}  energia {ef:.1f}")
print(f"termostato: final {ht[-1]:.2f}  oscilacao {oscilacao(ht):.2f}  energia {et:.1f}")
print([round(float(v), 1) for v in hf[::10]])
print([round(float(v), 1) for v in ht[::10]])
