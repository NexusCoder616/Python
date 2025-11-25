INF = 9999

def print_table(rt):
    for row in rt:
        print("  ".join(f"{x:4}" for x in row))
    print()

def distance_vector(graph, v):
    # initialize routing table
    rt = [[graph[i][j] for j in range(v)] for i in range(v)]

    # run DVR updates
    for _ in range(v * 3):
        for i in range(v):
            for j in range(v):
                for k in range(v):
                    if rt[i][k] + rt[k][j] < rt[i][j]:
                        rt[i][j] = rt[i][k] + rt[k][j]
    return rt


def main():
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    # Initialize graph with INF
    graph = [[INF] * v for _ in range(v)]
    for i in range(v):
        graph[i][i] = 0

    # Get edges
    for _ in range(e):
        s = int(input("Source: ")) - 1
        d = int(input("Destination: ")) - 1
        c = int(input("Cost: "))
        graph[s][d] = graph[d][s] = c

    print("\nInitial Routing Table:")
    rt = distance_vector(graph, v)
    print_table(rt)

    # Cost update
    print("Enter updated edge:")
    s = int(input("Source: ")) - 1
    d = int(input("Destination: ")) - 1
    c = int(input("New cost: "))
    graph[s][d] = graph[d][s] = c

    print("\nNew Routing Table:")
    rt = distance_vector(graph, v)
    print_table(rt)


if __name__ == "__main__":
    main()
