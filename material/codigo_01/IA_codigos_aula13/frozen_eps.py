import gymnasium as gym
from frozen_q import treinar, taxa_sucesso

env = gym.make("FrozenLake-v1", is_slippery=False)
casos = {"eps = 0 (nunca explora)": dict(eps0=0.0, eps_min=0.0),
         "eps fixo 0.9": dict(eps0=0.9, eps_min=0.9, decaimento=1.0),
         "eps fixo 0.1": dict(eps0=0.1, eps_min=0.1, decaimento=1.0),
         "eps decai de 1.0 a 0.05": dict()}
for nome, kw in casos.items():
    Q = treinar(env, 2000, **kw)
    print(nome, "-> sucesso:", taxa_sucesso(env, Q))
