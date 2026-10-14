import numpy as np

def tri(x, a, b, c):
    x = np.asarray(x, dtype=float)
    esq = (x - a) / (b - a) if b > a else (x >= a).astype(float)
    dir_ = (c - x) / (c - b) if c > b else (x <= c).astype(float)
    return np.clip(np.minimum(esq, dir_), 0, 1)

def trap(x, a, b, c, d):
    x = np.asarray(x, dtype=float)
    return np.clip(np.minimum(np.minimum((x - a) / (b - a), 1),
                              (d - x) / (d - c)), 0, 1)

def gauss(x, media, sigma):
    x = np.asarray(x, dtype=float)
    return np.exp(-((x - media) ** 2) / (2 * sigma ** 2))

if __name__ == "__main__":
    x = np.array([10, 15, 20, 25, 30])
    print(tri(x, 10, 20, 30))
    print(trap(x, 10, 15, 25, 30))
    print(np.round(gauss(x, 20, 5), 3))
