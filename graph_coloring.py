class GraphColoring:
    def __init__(self, vertices):
        """
        Initialize the graph with a given number of vertices.
        """
        self.V = vertices
        self.graph = []

    def add_edge(self, adjacency_matrix):
        """
        Add an adjacency matrix to the graph.
        """
        if len(adjacency_matrix) != self.V or any(len(row) != self.V for row in adjacency_matrix):
            raise ValueError("Invalid adjacency matrix size.")
        self.graph = adjacency_matrix

    def is_safe(self, v, color, c):
        """
        Check if assigning color `c` to vertex `v` is safe.
        """
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring_util(self, m, color, v):
        """
        Utility function to solve the graph coloring problem using backtracking.
        """
        if v == self.V:
            return True

       
        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c

                if self.graph_coloring_util(m, color, v + 1):
                    return True

             
                color[v] = 0

        return False

    def solve_coloring(self, m):
        """
        Solve the graph coloring problem.
        """
        color = [0] * self.V

        if not self.graph_coloring_util(m, color, 0):
            print("Solution does not exist.")
            return False

        self.print_solution(color)
        return True

    @staticmethod
    def print_solution(color):
        """
        Prints the assigned colors for the vertices.
        """
        print("Solution Exists: Following are the assigned colors:")
        print(" ".join(map(str, color)))



def main():
    print("Graph Coloring Problem")

   
    V = int(input("Enter the number of vertices: "))

   
    graph_coloring = GraphColoring(V)

    
    print("Enter the adjacency matrix row by row (space-separated):")
    adjacency_matrix = []
    for _ in range(V):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    graph_coloring.add_edge(adjacency_matrix)

    
    m = int(input("Enter the number of colors: "))

   
    graph_coloring.solve_coloring(m)


if __name__ == "__main__":
    main()
