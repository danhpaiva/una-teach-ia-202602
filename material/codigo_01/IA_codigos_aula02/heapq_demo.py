import heapq
fila = []
heapq.heappush(fila, (140, "Sibiu"))
heapq.heappush(fila, (80, "Rimnicu"))
print(heapq.heappop(fila))  # (80, 'Rimnicu')
