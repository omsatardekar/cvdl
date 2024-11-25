from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printVertexCover(self):
        visited = [False] * self.V

        for u in range(self.V):
            if not visited[u]:
                for v in self.graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        visited[u] = True
                        break

        for j in range(self.V):
            if visited[j]:
                print(j, end=" ")
        print()


# Input for the graph
V = int(input("Enter the number of vertices: "))
g = Graph(V)

E = int(input("Enter the number of edges: "))
print("Enter the edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.addEdge(u, v)

g.printVertexCover()
