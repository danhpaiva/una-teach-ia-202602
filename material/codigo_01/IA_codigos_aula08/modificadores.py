import math

mu = 0.7   # "quente" a 28 graus
print("quente           :", mu)
print("muito quente     :", round(mu ** 2, 2))
print("mais ou menos    :", round(math.sqrt(mu), 2))
print("nada quente      :", round(1 - mu, 2))
