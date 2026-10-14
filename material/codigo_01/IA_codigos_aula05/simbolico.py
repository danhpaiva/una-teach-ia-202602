def num(v):
    return isinstance(v, (int, float))

def simplificar(e):
    if not isinstance(e, tuple):
        return e
    op, a, b = e[0], simplificar(e[1]), simplificar(e[2])
    if op == "+" and a == 0:
        return b
    if op == "+" and b == 0:
        return a
    if op == "*" and (a == 0 or b == 0):
        return 0
    if op == "*" and a == 1:
        return b
    if op == "*" and b == 1:
        return a
    if op == "^" and b == 1:
        return a
    if num(a) and num(b) and op in ("+", "*"):
        return {"+": a + b, "*": a * b}[op]
    return (op, a, b)

def derivar(e, v="x"):
    if isinstance(e, (int, float)):
        return 0
    if isinstance(e, str):
        return 1 if e == v else 0
    op, a, b = e
    if op == "+":
        return ("+", derivar(a, v), derivar(b, v))
    if op == "*":
        return ("+", ("*", derivar(a, v), b), ("*", a, derivar(b, v)))
    if op == "^":
        return ("*", ("*", b, ("^", a, b - 1)), derivar(a, v))

def mostrar(e):
    if not isinstance(e, tuple):
        return str(e)
    op, a, b = e
    return f"({mostrar(a)} {op} {mostrar(b)})"

if __name__ == "__main__":
    print(mostrar(simplificar(("+", ("*", 1, "x"), 0))))
    print(mostrar(simplificar(("*", ("+", 2, 3), "x"))))
    f = ("+", ("^", "x", 3), ("*", 5, "x"))
    d = derivar(f)
    print(mostrar(d))
    print(mostrar(simplificar(d)))
    from expr import avaliar
    print(avaliar(simplificar(d), {"x": 2}))
