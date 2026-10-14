def eh_var(t):
    return isinstance(t, str) and t[:1].isupper()

def walk(t, s):
    while eh_var(t) and t in s:
        t = s[t]
    return t

def unificar(a, b, s):
    if s is None:
        return None
    a, b = walk(a, s), walk(b, s)
    if a == b:
        return s
    if eh_var(a):
        return {**s, a: b}
    if eh_var(b):
        return {**s, b: a}
    if isinstance(a, tuple) and isinstance(b, tuple) and len(a) == len(b):
        for x, y in zip(a, b):
            s = unificar(x, y, s)
        return s
    return None

if __name__ == "__main__":
    print(unificar(("pai", "X", "maria"), ("pai", "joao", "maria"), {}))
    print(unificar(("pai", "X", "Y"), ("pai", "joao", "maria"), {}))
    print(unificar(("pai", "joao", "maria"), ("pai", "pedro", "maria"), {}))
    print(unificar(("pai", "X", "X"), ("pai", "joao", "maria"), {}))
