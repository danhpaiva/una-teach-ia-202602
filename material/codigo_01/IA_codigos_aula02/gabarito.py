# Gabarito da Aula 02. Exercicio 1 (seu proprio labirinto) nao tem resposta unica:
# edite LABIRINTO em busca.py e compare os tres algoritmos.
import heapq
from busca import LABIRINTO, achar, vizinhos, caminho, manhattan, bfs, dfs, a_estrela

def a_estrela_h(grade, h_fn, vizinhos_fn=vizinhos):
    inicio, meta = achar(grade, "S"), achar(grade, "G")
    h0 = h_fn(inicio, meta)
    fronteira = [(h0, h0, 0, inicio)]
    pais = {inicio: None}
    custo = {inicio: 0}
    expandidos = 0
    while fronteira:
        _, _, g, atual = heapq.heappop(fronteira)
        expandidos += 1
        if atual == meta:
            return caminho(pais, atual), expandidos
        for viz in vizinhos_fn(grade, atual):
            novo_g = g + 1
            if viz not in custo or novo_g < custo[viz]:
                custo[viz] = novo_g
                pais[viz] = atual
                h = h_fn(viz, meta)
                heapq.heappush(fronteira, (novo_g + h, h, novo_g, viz))

def gulosa(grade):
    inicio, meta = achar(grade, "S"), achar(grade, "G")
    fronteira = [(manhattan(inicio, meta), inicio)]
    pais = {inicio: None}
    expandidos = 0
    while fronteira:
        _, atual = heapq.heappop(fronteira)
        expandidos += 1
        if atual == meta:
            return caminho(pais, atual), expandidos
        for viz in vizinhos(grade, atual):
            if viz not in pais:
                pais[viz] = atual
                heapq.heappush(fronteira, (manhattan(viz, meta), viz))

def vizinhos8(grade, pos):
    r, c = pos
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (dr or dc) and grade[r + dr][c + dc] != "#":
                yield (r + dr, c + dc)

def chebyshev(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def mostrar(nome, resultado):
    rota, exp = resultado
    print(f"{nome:28} passos={len(rota) - 1:3}  expandidos={exp}")

print("Exercicio 1: compare os tres no seu labirinto")
for nome, f in [("BFS", bfs), ("DFS", dfs), ("A*", a_estrela)]:
    mostrar(nome, f(LABIRINTO))
print("Exercicio 2: A* com h = 0")
mostrar("A* com h=0", a_estrela_h(LABIRINTO, lambda a, b: 0))
print("Exercicio 3: busca gulosa")
mostrar("gulosa", gulosa(LABIRINTO))
print("Exercicio 4: 8 movimentos")
mostrar("A* diagonal + Chebyshev", a_estrela_h(LABIRINTO, chebyshev, vizinhos8))
mostrar("A* diagonal + Manhattan", a_estrela_h(LABIRINTO, manhattan, vizinhos8))
