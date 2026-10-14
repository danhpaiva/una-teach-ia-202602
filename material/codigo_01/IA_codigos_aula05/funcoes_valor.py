def dobro(x):
    return x * 2

def aplicar_duas_vezes(f, x):
    return f(f(x))

def criar_multiplicador(n):
    return lambda x: x * n

triplo = criar_multiplicador(3)
print(aplicar_duas_vezes(dobro, 5))
print(triplo(7))
print(aplicar_duas_vezes(triplo, 2))
