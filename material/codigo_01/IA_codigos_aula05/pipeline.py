from functools import reduce

def compor(*fs):
    return reduce(lambda f, g: lambda x: g(f(x)), fs)

limpar = compor(str.strip, str.lower, lambda s: s.replace("  ", " "))
print(limpar("  OLA  Mundo  "))
