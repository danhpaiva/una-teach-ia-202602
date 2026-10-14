from pertinencia import tri
from mamdani_manual import gorjeta
from ar_condicionado import potencia

# Exercicio 1: pertinencia de 25 no termo "agradavel"
print("ex1:", tri(25, 15, 22, 29))              # (29 - 25) / (29 - 22) = 4/7

# Exercicio 2: E e OU fuzzy (quente = 0,2; umido = 0,9)
print("ex2: E =", min(0.2, 0.9), " OU =", max(0.2, 0.9))

# Exercicio 3: gorjetas
print("ex3:", round(gorjeta(5, 10), 2), round(gorjeta(2, 2), 2))

# Exercicio 4: potencia do ar-condicionado
print("ex4:", round(potencia(3.0), 1), round(potencia(0.5), 1),
      round(potencia(-2.0), 1))
