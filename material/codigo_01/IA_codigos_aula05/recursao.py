def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

def soma_lista(xs):
    if not xs:
        return 0
    return xs[0] + soma_lista(xs[1:])

print(fatorial(5), soma_lista([3, 1, 4, 1, 5]))
