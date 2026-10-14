alunos = [("Ana", 8.5), ("Bruno", 6.0), ("Carla", 9.2)]
por_nota = sorted(alunos, key=lambda a: a[1], reverse=True)
print(por_nota)
