import numpy as np
from pertinencia import tri, gauss

serv = np.linspace(0, 10, 101)
comi = np.linspace(0, 10, 101)
gorj = np.linspace(0, 25, 251)

# conjuntos de entrada (como funcoes) e de saida (como vetores)
servico_ruim  = lambda s: gauss(s, 0, 1.5)
servico_medio = lambda s: gauss(s, 5, 1.5)
servico_bom   = lambda s: gauss(s, 10, 1.5)
comida_ruim   = lambda c: tri(c, 0, 0, 5)
comida_boa    = lambda c: tri(c, 5, 10, 10)
baixa = tri(gorj, 0, 0, 13)
media = tri(gorj, 0, 13, 25)
alta  = tri(gorj, 13, 25, 25)

def gorjeta(servico, comida, detalhe=False):
    # 1) fuzzificacao + regras (OU = max)
    f1 = float(max(comida_ruim(comida), servico_ruim(servico)))
    f2 = float(servico_medio(servico))
    f3 = float(max(comida_boa(comida), servico_bom(servico)))
    # 2) implicacao: corta cada saida no grau da regra (min)
    # 3) agregacao: uniao das saidas (max)
    agregada = np.maximum.reduce([np.minimum(f1, baixa),
                                  np.minimum(f2, media),
                                  np.minimum(f3, alta)])
    # 4) defuzzificacao: centroide
    saida = (gorj * agregada).sum() / agregada.sum()
    return (f1, f2, f3, saida) if detalhe else saida

if __name__ == "__main__":
    for s, c in [(3, 2), (6.5, 9.0), (9.8, 9.5)]:
        f1, f2, f3, g = gorjeta(s, c, detalhe=True)
        print(f"servico={s} comida={c}: f1={f1:.2f} f2={f2:.2f} f3={f3:.2f} -> {g:.2f}%")
