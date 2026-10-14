import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False)
print("estados:", env.observation_space, " acoes:", env.action_space)
estado, info = env.reset(seed=0)
print("estado inicial:", estado)
for acao in (2, 2, 1, 1, 1, 2):          # 0 esq, 1 baixo, 2 dir, 3 cima
    estado, r, terminou, truncou, info = env.step(acao)
    print("acao", acao, "-> estado", estado, "recompensa", r,
          "terminou", terminou, "truncou", truncou)
    if terminou or truncou:
        break
