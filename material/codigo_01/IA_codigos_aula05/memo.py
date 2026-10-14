from functools import lru_cache

chamadas = 0

def fib(n):
    global chamadas
    chamadas += 1
    return n if n < 2 else fib(n - 1) + fib(n - 2)

fib(25)
print(chamadas)

chamadas = 0

@lru_cache(maxsize=None)
def fibm(n):
    global chamadas
    chamadas += 1
    return n if n < 2 else fibm(n - 1) + fibm(n - 2)

fibm(25)
print(chamadas)
