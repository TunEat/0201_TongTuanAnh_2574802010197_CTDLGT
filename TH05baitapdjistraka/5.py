#bài 5 đồ thị vô hướng có trọng số
import heapq

graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 6)],
    'D': [('B', 2), ('C', 6), ('E', 4)],
    'E': [('D', 4)]
}

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            nd = dist[u] + w

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist

print(dijkstra(graph, 'A'))