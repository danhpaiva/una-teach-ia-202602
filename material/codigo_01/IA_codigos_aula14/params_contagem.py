def dense(n_in, n_out):
    return (n_in + 1) * n_out

def conv(k, c_in, filtros):
    return (k * k * c_in + 1) * filtros

def saida_conv(n, k):
    return n - k + 1

d1, d2 = dense(784, 128), dense(128, 10)
print("MLP: Dense(784 -> 128) =", d1, "| Dense(128 -> 10) =", d2)
print("     total =", d1 + d2)

n = 28
n = saida_conv(n, 3); print("apos Conv2D 3x3:", n)
n = n // 2;           print("apos MaxPooling 2x2:", n)
n = saida_conv(n, 3); print("apos Conv2D 3x3:", n)
n = n // 2;           print("apos MaxPooling 2x2:", n)
entrada_dense = n * n * 64
print("Flatten:", n, "x", n, "x 64 =", entrada_dense)

c1, c2, d = conv(3, 1, 32), conv(3, 32, 64), dense(entrada_dense, 10)
print("CNN: Conv2D(32) =", c1, "| Conv2D(64) =", c2, "| Dense(10) =", d)
print("     total =", c1 + c2 + d)
