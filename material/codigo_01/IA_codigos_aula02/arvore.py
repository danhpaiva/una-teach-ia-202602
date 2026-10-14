from collections import deque

ARVORE = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G"],
    "D": ["H"],
}

def bfs_ordem(grafo, inicio):
    fronteira = deque([inicio])
    ordem = []
    while fronteira:
        no = fronteira.popleft()
        ordem.append(no)
        fronteira.extend(grafo.get(no, []))
    return ordem

def dfs_ordem(grafo, inicio):
    fronteira = [inicio]
    ordem = []
    while fronteira:
        no = fronteira.pop()
        ordem.append(no)
        fronteira.extend(reversed(grafo.get(no, [])))
    return ordem

print("BFS:", bfs_ordem(ARVORE, "A"))
print("DFS:", dfs_ordem(ARVORE, "A"))
