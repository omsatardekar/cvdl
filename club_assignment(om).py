import sys

def clubAssignment(cost_matrix):
    
    n = len(cost_matrix)  
    assignment = [-1] * n

    min_cost = sys.maxsize

    def solve(level, current_cost, club_assigned):
        nonlocal min_cost, assignment

        if level == n:
            min_cost = current_cost
            assignment = list(club_assigned)
            return

        for club in range(n):
            if club not in club_assigned:
                
                temp_cost = current_cost + cost_matrix[level][club]

                if temp_cost < min_cost:
                    club_assigned[level] = club 
                    solve(level + 1, temp_cost, club_assigned)
                    club_assigned[level] = -1  

  
    solve(0, 0, [-1] * n)

    final_assignment = []  
    for i in range(n):  
        final_assignment.append((i, assignment[i]))  
    return min_cost, final_assignment


N = int(input("Enter the number of students and clubs (N): "))
print(f"Enter the cost matrix ({N}x{N}):")
cost_matrix = []
for i in range(N):
    cost_matrix.append(list(map(int, input(f"Row {i + 1}: ").split())))

min_cost, assignment = clubAssignment(cost_matrix)

print("\nMinimum total cost:", min_cost)
print("Optimal assignment (Student -> Club):")
for student, club in assignment:
    print(f"Student {student} -> Club {club}")
