import math
import random

def rastrigin(x, y):
    return (20 + x * x + y * y
            - 10 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))

LIM = 5.12
W, C1, C2 = 0.7, 1.5, 1.5

def pso(n_part=20, iteracoes=50):
    pos = [[random.uniform(-LIM, LIM), random.uniform(-LIM, LIM)]
           for _ in range(n_part)]
    vel = [[0.0, 0.0] for _ in range(n_part)]
    pbest = [p[:] for p in pos]
    gbest = min(pbest, key=lambda p: rastrigin(*p))[:]
    for it in range(iteracoes + 1):
        if it % 10 == 0:
            print(f"iter {it:2}: melhor f = {rastrigin(*gbest):.4f}")
        for i in range(n_part):
            for d in range(2):
                r1, r2 = random.random(), random.random()
                vel[i][d] = (W * vel[i][d]
                             + C1 * r1 * (pbest[i][d] - pos[i][d])
                             + C2 * r2 * (gbest[d] - pos[i][d]))
                pos[i][d] = max(-LIM, min(LIM, pos[i][d] + vel[i][d]))
            if rastrigin(*pos[i]) < rastrigin(*pbest[i]):
                pbest[i] = pos[i][:]
                if rastrigin(*pbest[i]) < rastrigin(*gbest):
                    gbest = pbest[i][:]
    return gbest

if __name__ == "__main__":
    random.seed(7)
    g = pso()
    print([round(v, 3) for v in g], round(rastrigin(*g), 4))
