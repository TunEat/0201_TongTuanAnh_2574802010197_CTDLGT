#bài 3 Dijkstra cơ bản :nguồn tới mọi đỉnh
adj = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3), (5, 6)],
    [(5, 2)],
    []
]
def dijkstra(adj, s):
    n = len(adj)
    dist = [float('inf')] * n #khởi tạo danh sách
    visited = [False] * n
    dist[s] = 0
    for i in range(n):
        u = -1
        minn = float('inf')

        for j in range(n):
            if not visited[j] and dist[j] < minn:
                minn = dist[j]
                u = j
        if u == -1:
            break

        visited[u] = True

        for v, w in adj[u]:
            if not visited[v] and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    return dist
print(dijkstra(adj, 0))