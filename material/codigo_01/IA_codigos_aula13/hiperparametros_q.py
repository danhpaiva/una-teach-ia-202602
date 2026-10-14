import numpy as np
from qlearning_grid import treinar

def media_final(**kw):
    runs = [treinar(seed=s, **kw)[1] for s in range(5)]
    return float(np.mean([np.mean(r[-50:]) for r in runs]))

print("alfa (gamma 0.9, eps decai):")
for alfa in (0.01, 0.1, 0.5, 1.0):
    print(" ", alfa, round(media_final(alfa=alfa), 2))
print("gamma (alfa 0.1):")
for gamma in (0.0, 0.5, 0.9, 0.99):
    print(" ", gamma, round(media_final(gamma=gamma), 2))
print("exploracao (alfa 0.1, gamma 0.9):")
casos = (("eps fixo 0.5", dict(eps0=0.5, eps_min=0.5, decaimento=1.0)),
         ("eps fixo 0.05", dict(eps0=0.05, eps_min=0.05, decaimento=1.0)),
         ("eps decai de 1.0 a 0.05", dict()))
for nome, kw in casos:
    print(" ", nome, round(media_final(**kw), 2))
