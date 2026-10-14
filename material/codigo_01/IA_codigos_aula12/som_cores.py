import numpy as np
from minisom import MiniSom

rng = np.random.default_rng(0)
cores = rng.random((200, 3))                  # 200 cores RGB aleatorias
som = MiniSom(10, 10, 3, sigma=3.0, learning_rate=0.5, random_seed=0)
print("erro antes :", round(som.quantization_error(cores), 3))
som.train_random(cores, 5000)
print("erro depois:", round(som.quantization_error(cores), 3))
print("cor do neuronio (0, 0):", np.round(som.get_weights()[0, 0], 2))
print("cor do neuronio (0, 1):", np.round(som.get_weights()[0, 1], 2))
