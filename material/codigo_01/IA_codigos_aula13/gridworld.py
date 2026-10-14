import numpy as np

ACOES = ["cima", "direita", "baixo", "esquerda"]
MOVE = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class GridWorld:
    """Grade 4x4. Inicio (0, 0), meta (3, 3) = +10, armadilha (1, 3) = -10."""
    def __init__(self):
        self.n = 4
        self.meta, self.armadilha = (3, 3), (1, 3)
        self.pos = (0, 0)

    def reset(self):
        self.pos = (0, 0)
        return self.estado()

    def estado(self):
        return self.pos[0] * self.n + self.pos[1]

    def step(self, acao):
        dl, dc = MOVE[acao]
        l = min(max(self.pos[0] + dl, 0), self.n - 1)
        c = min(max(self.pos[1] + dc, 0), self.n - 1)
        self.pos = (l, c)
        if self.pos == self.meta:
            return self.estado(), 10, True
        if self.pos == self.armadilha:
            return self.estado(), -10, True
        return self.estado(), -1, False

if __name__ == "__main__":
    env = GridWorld()
    print("estado inicial:", env.reset())
    for a in (1, 1, 2, 2, 2, 1):
        s, r, fim = env.step(a)
        print(ACOES[a], "-> estado", s, "recompensa", r, "fim", fim)
