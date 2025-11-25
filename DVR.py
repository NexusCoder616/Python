INF = 999
v = int(input("Vertices: "))
dist = [[INF]*v for _ in range(v)]

for i in range(v):
    dist[i][i] = 0

e = int(input("Edges: "))
for _ in range(e):
    s = int(input("Enter Source:"))-1
    d = int(input("Enter Destination":))-1
    c = int(input("Enter Cost:"))
    dist[s][d] = dist[d][s] = c

for _ in range(v):
    for i in range(v):
        for j in range(v):
            for k in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for r in dist:
    print(r)