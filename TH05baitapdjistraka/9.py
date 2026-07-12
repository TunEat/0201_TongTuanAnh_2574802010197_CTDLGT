#bài 9
import heapq

def dijkstra_heap(graph, start):

    n = len(graph)

    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0,start)]

    while pq:

        d,u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v,w in graph[u]:

            nd = dist[u] + w

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq,(nd,v))

    return dist