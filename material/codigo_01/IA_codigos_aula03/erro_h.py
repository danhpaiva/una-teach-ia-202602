def f(x):
    return x ** 2

for h in [1e-1, 1e-3, 1e-6, 1e-9, 1e-12, 1e-15]:
    d = (f(3 + h) - f(3)) / h
    print(f"{h:.0e}  {d:.10f}  erro={abs(d - 6):.2e}")
