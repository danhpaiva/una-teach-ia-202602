import math

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

for x in [-10, -2, 0, 2, 10]:
    print(x, sigmoide(x))
