total = 0

def soma_impura(x):
    global total
    total += x
    return total

def soma_pura(a, b):
    return a + b

print(soma_impura(5), soma_impura(5))
print(soma_pura(5, 5), soma_pura(5, 5))
