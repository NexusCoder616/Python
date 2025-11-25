INF = 9999

def bf(g, s):
    d = g[s][:]
    n = len(g)
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if d[u] + g[u][v] < d[v]:
                    d[v] = d[u] + g[u][v]
    return d

n = int(input("Enter number of nodes: "))
g = [list(map(int, input().split())) for _ in range(n)]
g = [[INF if x == -1 else x for x in r] for r in g]

print("\n--- Distance Vector Tables ---\n")

for i in range(n):
    print(f"Node {i} Distance Vector:", bf(g, i))
