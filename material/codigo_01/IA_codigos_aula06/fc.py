def combinar(cf1, cf2):
    return cf1 + cf2 * (1 - cf1)

print(round(combinar(0.6, 0.5), 2))
print(round(combinar(0.6, 0.0), 2))
print(round(combinar(combinar(0.6, 0.5), 0.4), 3))
print(round(min(0.8, 0.6) * 0.9, 3))
