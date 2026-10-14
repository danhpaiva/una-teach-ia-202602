dom = ["ana", "bruno", "carla"]
humano = {"ana", "bruno", "carla"}
mortal = {"ana", "bruno", "carla"}
aluno = {"ana", "bruno"}
aprov = {"ana"}

def implica(p, q):
    return (not p) or q

# para todo x: humano(x) -> mortal(x)
print(all(implica(x in humano, x in mortal) for x in dom))
# existe x: aluno(x) e aprov(x)
print(any(x in aluno and x in aprov for x in dom))
# para todo x: aluno(x) -> aprov(x)
print(all(implica(x in aluno, x in aprov) for x in dom))
# armadilha: para todo x: aluno(x) E aprov(x)
print(all(x in aluno and x in aprov for x in dom))
# armadilha: existe x: aluno(x) -> aprov(x)
print(any(implica(x in aluno, x in aprov) for x in dom))
