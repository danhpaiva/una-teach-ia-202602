OBJETIVO = (1, 2, 3, 4, 5, 6, 7, 8, 0)
estado   = (7, 2, 4, 5, 0, 6, 8, 3, 1)

def manhattan_puzzle(e):
    total = 0
    for i, v in enumerate(e):
        if v != 0:
            j = OBJETIVO.index(v)
            total += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return total

print(manhattan_puzzle(estado))
