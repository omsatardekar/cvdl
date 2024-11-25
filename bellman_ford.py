class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src):
        
        dist = [float("Inf")] * self.V
        dist[src] = 0

        
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

       
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

       
        self.printArr(dist)


def main():
    
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    
    edges = int(input("Enter the number of edges: "))
    print("Enter each edge in the format: u v w (source, destination, weight)")

    for _ in range(edges):
        try:
            u, v, w = map(int, input("Enter edge (u v w): ").split())
            g.addEdge(u, v, w)
        except ValueError:
            print("Invalid format. Please enter the edge again.")
            continue

   
    src = int(input("Enter the source vertex: "))
    print("\nRunning Bellman-Ford Algorithm...\n")
    g.BellmanFord(src)


if __name__ == "__main__":
    main()
