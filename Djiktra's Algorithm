import heapq

def dijkstra(g, s):
    d = {n: float('inf') for n in g}
    d[s] = 0
    pq = [(0, s)]

    while pq:
        dist, node = heapq.heappop(pq)

        if dist > d[node]:
            continue

        for nb, w in g[node].items():
            nd = dist + w
            if nd < d[nb]:
                d[nb] = nd
                heapq.heappush(pq, (nd, nb))

    return d


g = {}

for _ in range(int(input("Nodes: "))):
    g[input().strip()] = {}

for _ in range(int(input("Edges: "))):
    u, v, w = input().split()
    w = int(w)
    g[u][v] = g[v][u] = w

s = input("Start: ").strip()

for n, d in dijkstra(g, s).items():
    print(f"{s} → {n} = {d}")
