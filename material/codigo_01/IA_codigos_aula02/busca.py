from collections import deque
import heapq

LABIRINTO = [
    "###############",
    "#S............#",
    "#.............#",
    "#.....#.......#",
    "#.....#.......#",
    "#.....#.......#",
    "#.....#.......#",
    "#.....#####...#",
    "#.............#",
    "#............G#",
    "###############",
]

def achar(grade, simbolo):
    for r, linha in enumerate(grade):
        if simbolo in linha:
            return (r, linha.index(simbolo))

def vizinhos(grade, pos):
    r, c = pos
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if grade[nr][nc] != "#":
            yield (nr, nc)

def caminho(pais, fim):
    rota = [fim]
    while pais[rota[-1]] is not None:
        rota.append(pais[rota[-1]])
    return rota[::-1]

def bfs(grade):
    inicio, meta = achar(grade, "S"), achar(grade, "G")
    fronteira = deque([inicio])
    pais = {inicio: None}
    expandidos = 0
    while fronteira:
        atual = fronteira.popleft()
        expandidos += 1
        if atual == meta:
            return caminho(pais, atual), expandidos
        for viz in vizinhos(grade, atual):
            if viz not in pais:
                pais[viz] = atual
                fronteira.append(viz)

def dfs(grade):
    inicio, meta = achar(grade, "S"), achar(grade, "G")
    fronteira = [inicio]
    pais = {inicio: None}
    expandidos = 0
    while fronteira:
        atual = fronteira.pop()
        expandidos += 1
        if atual == meta:
            return caminho(pais, atual), expandidos
        for viz in vizinhos(grade, atual):
            if viz not in pais:
                pais[viz] = atual
                fronteira.append(viz)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_estrela(grade):
    inicio, meta = achar(grade, "S"), achar(grade, "G")
    h0 = manhattan(inicio, meta)
    fronteira = [(h0, h0, 0, inicio)]
    pais = {inicio: None}
    custo = {inicio: 0}
    expandidos = 0
    while fronteira:
        _, _, g, atual = heapq.heappop(fronteira)
        expandidos += 1
        if atual == meta:
            return caminho(pais, atual), expandidos
        for viz in vizinhos(grade, atual):
            novo_g = g + 1
            if viz not in custo or novo_g < custo[viz]:
                custo[viz] = novo_g
                pais[viz] = atual
                h = manhattan(viz, meta)
                heapq.heappush(fronteira, (novo_g + h, h, novo_g, viz))

if __name__ == "__main__":
    for nome, algoritmo in [("BFS", bfs), ("DFS", dfs), ("A*", a_estrela)]:
        rota, exp = algoritmo(LABIRINTO)
        print(f"{nome:4} passos={len(rota) - 1:3}  expandidos={exp}")
