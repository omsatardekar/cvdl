import heapq
import copy


class Node:
    def __init__(self, worker_id, job_id, assigned, parent):
        self.parent = parent  
        self.pathCost = 0  
        self.cost = 0  
        self.workerID = worker_id  
        self.jobID = job_id  
        self.assigned = copy.deepcopy(assigned)  

        
        if job_id != -1:
            self.assigned[job_id] = True


class CustomHeap:
    """Custom heap for maintaining nodes with costs."""

    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, (node.cost, node))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None


def calculate_cost(cost_matrix, x, assigned):
    """
    Calculate the estimated cost of assigning jobs.
    """
    N = len(cost_matrix)
    cost = 0
    available = [True] * N

   
    for j in range(N):
        if assigned[j]:
            available[j] = False

    
    for i in range(x + 1, N):
        min_val = float('inf')
        for j in range(N):
            if available[j] and cost_matrix[i][j] < min_val:
                min_val = cost_matrix[i][j]
        cost += min_val
    return cost


def new_node(x, y, assigned, parent, cost_matrix):
    """
    Create a new search tree node.
    """
    node = Node(x, y, assigned, parent)
    if x != -1:
        node.pathCost = parent.pathCost + cost_matrix[x][y]
        node.cost = node.pathCost + calculate_cost(cost_matrix, x, node.assigned)
    return node


def print_assignments(node):
    """
    Print the job assignments from the solution node.
    """
    if node.parent is None:
        return
    print_assignments(node.parent)
    print(f"Assign Worker {chr(node.workerID + 65)} to Job {node.jobID}")


def find_min_cost(cost_matrix):
    """
    Solve the Job Assignment Problem using Branch and Bound.
    """
    N = len(cost_matrix)
    assigned = [False] * N
    pq = CustomHeap()

    
    root = new_node(-1, -1, assigned, None, cost_matrix)
    root.cost = 0
    pq.push(root)

 
    while True:
        
        min_node = pq.pop()

        
        if min_node.workerID == N - 1:
            print_assignments(min_node)
            return min_node.pathCost

      
        for i in range(N):
            if not min_node.assigned[i]:
                child = new_node(min_node.workerID + 1, i, min_node.assigned, min_node, cost_matrix)
                pq.push(child)


def main():
    """
    User-driven driver code for the Job Assignment Problem.
    """
  
    print("Enter the number of workers/jobs (N): ", end="")
    N = int(input().strip())

    print("\nEnter the cost matrix row by row (space-separated values):")
    cost_matrix = []
    for i in range(N):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != N:
            print("Invalid row size. Please ensure each row has exactly N elements.")
            return
        cost_matrix.append(row)

   
    print("\nFinding the optimal assignment...\n")
    optimal_cost = find_min_cost(cost_matrix)
    print(f"\nOptimal Cost is {optimal_cost}")


if __name__ == "__main__":
    main()
