expr = ("*", ("+", "x", 2), 3)

def avaliar(e, env):
    if isinstance(e, (int, float)):
        return e
    if isinstance(e, str):
        return env[e]
    op, a, b = e
    va, vb = avaliar(a, env), avaliar(b, env)
    return {"+": va + vb, "-": va - vb, "*": va * vb, "^": va ** vb}[op]

print(avaliar(expr, {"x": 4}))
