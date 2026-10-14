a = 0.7   # "quente" a 28 graus
b = 0.4   # "umido"

print("E  (min):", min(a, b))
print("OU (max):", max(a, b))
print("NAO     :", round(1 - a, 2))
print("E  (produto):", round(a * b, 2))
print("OU (soma prob.):", round(a + b - a * b, 2))
