from sympy import symbols, diff, simplify, expand, solve

x = symbols("x")
f = x**3 + 5*x
print(diff(f, x))
print(expand((x + 2) * 3))
print(simplify((x**2 - 1) / (x - 1)))
print(solve(x**2 - 4, x))
