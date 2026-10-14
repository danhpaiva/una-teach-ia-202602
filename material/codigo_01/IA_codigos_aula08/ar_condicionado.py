import numpy as np
from pertinencia import tri

erro_u = np.linspace(-6, 10, 161)
pot_u = np.linspace(0, 100, 1001)

# erro = temperatura - alvo (graus)
def mu_erro(e):
    return {"negativo": float(tri(e, -6, -6, 0)),
            "zero": float(tri(e, -1.5, 0, 1.5)),
            "pequeno": float(tri(e, 0, 2, 4)),
            "grande": float(tri(e, 2, 6, 10))}

saidas = {"desligar": tri(pot_u, 0, 0, 15),
          "baixa": tri(pot_u, 5, 25, 45),
          "media": tri(pot_u, 30, 55, 80),
          "alta": tri(pot_u, 60, 100, 100)}
regra = {"negativo": "desligar", "zero": "baixa",
         "pequeno": "media", "grande": "alta"}

def potencia(erro):
    graus = mu_erro(min(max(erro, -6), 10))
    agregada = np.maximum.reduce(
        [np.minimum(g, saidas[regra[k]]) for k, g in graus.items()])
    if agregada.sum() == 0:
        return 0.0
    return (pot_u * agregada).sum() / agregada.sum()

if __name__ == "__main__":
    for e in [-3, -1, 0, 1, 2, 4, 7]:
        print(f"erro={e:+d}: {potencia(e):5.1f}%")
