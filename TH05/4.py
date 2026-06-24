#bài 4 in khoảng cách tới mọi đỉnh
INF = float('inf')

# Đồ thị G1
adj = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5), (4,8)],
    3: [(4,3), (5,5)],
    4: [(5,2)],
    5: []
}

def dijkstra(adj, s):
    n = len(adj)

    dist = [INF] * n
    visited = [False] * n

    dist[s] = 0

    for _ in range(n):
        u = -1

        # tìm đỉnh chưa xét có dist nhỏ nhất
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        if u == -1:
            break

        visited[u] = True

        # relax các cạnh kề
        for v, w in adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

# nguồn
s = 0

dist = dijkstra(adj, s)

print("Khoảng cách từ đỉnh", s)

for i in range(len(dist)):
    if dist[i] == INF:
        print(f"dist[{i}] = -1")
    else:
        print(f"dist[{i}] = {dist[i]}")