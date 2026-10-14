import heapq

MAPA = {
    "Arad":      {"Sibiu": 140},
    "Sibiu":     {"Arad": 140, "Fagaras": 99, "Rimnicu": 80},
    "Fagaras":   {"Sibiu": 99, "Bucareste": 211},
    "Rimnicu":   {"Sibiu": 80, "Pitesti": 97},
    "Pitesti":   {"Rimnicu": 97, "Bucareste": 101},
    "Bucareste": {"Fagaras": 211, "Pitesti": 101},
}

# distância em linha reta até Bucareste (heurística)
H = {"Arad": 366, "Sibiu": 253, "Fagaras": 176,
     "Rimnicu": 193, "Pitesti": 100, "Bucareste": 0}

def buscar(inicio, meta, prioridade):
    fronteira = [(prioridade(0, inicio), 0, inicio, [inicio])]
    explorados = set()
    while fronteira:
        _, g, cidade, rota = heapq.heappop(fronteira)
        if cidade in explorados:
            continue
        explorados.add(cidade)
        if cidade == meta:
            return rota, g
        for viz, passo in MAPA[cidade].items():
            novo_g = g + passo
            heapq.heappush(fronteira,
                (prioridade(novo_g, viz), novo_g, viz, rota + [viz]))

custo_uniforme = lambda g, cidade: g
gulosa         = lambda g, cidade: H[cidade]
a_estrela      = lambda g, cidade: g + H[cidade]

for nome, f in [("Custo uniforme", custo_uniforme), ("Gulosa", gulosa), ("A*", a_estrela)]:
    rota, custo = buscar("Arad", "Bucareste", f)
    print(f"{nome:15} custo={custo}  {' > '.join(rota)}")
