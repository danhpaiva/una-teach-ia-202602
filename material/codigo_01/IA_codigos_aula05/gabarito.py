from functools import reduce
from simbolico import derivar, simplificar, mostrar
from unify import unificar

# Exercicio 1: soma dos quadrados dos impares de 1 a 9
impares = filter(lambda x: x % 2 == 1, range(1, 10))
quad = map(lambda x: x ** 2, impares)
print("ex1:", reduce(lambda a, x: a + x, quad, 0))        # 165

# Exercicio 2: potencia recursiva
def potencia(b, n):
    if n == 0:
        return 1
    return b * potencia(b, n - 1)

print("ex2:", potencia(2, 10))                            # 1024

# Exercicio 3: derivar 3x^2 + 2x, simplificar e avaliar em x = 2
def avaliar(e, env):
    if isinstance(e, (int, float)):
        return e
    if isinstance(e, str):
        return env[e]
    op, a, b = e
    va, vb = avaliar(a, env), avaliar(b, env)
    return {"+": va + vb, "-": va - vb,
            "*": va * vb, "^": va ** vb}[op]

f = ("+", ("*", 3, ("^", "x", 2)), ("*", 2, "x"))
d = simplificar(derivar(f))
print("ex3:", mostrar(d), "=", avaliar(d, {"x": 2}))      # 14

# Exercicio 4: unificar pai(X, Y) com pai(Y, maria)
s = unificar(("pai", "X", "Y"), ("pai", "Y", "maria"), {})
print("ex4:", s)    # X -> Y e Y -> maria, logo X = maria
