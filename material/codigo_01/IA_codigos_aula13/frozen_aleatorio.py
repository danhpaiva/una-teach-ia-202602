import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False)
env.action_space.seed(0)
sucessos, episodios = 0, 2000
for ep in range(episodios):
    s, _ = env.reset(seed=ep)
    fim = False
    while not fim:
        s, r, term, trunc, _ = env.step(env.action_space.sample())
        fim = term or trunc
    sucessos += r
print("agente aleatorio: meta em", int(sucessos), "de", episodios)
