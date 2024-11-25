def knapsack(profit, weights, capacity):
    n = len(profit)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + profit[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]



def main():
    print("Welcome to the Knapsack Problem Solver!")
    
   
    profit = list(map(int, input("Enter the profits (comma-separated): ").split(',')))
    
   
    weights = list(map(int, input("Enter the weights (comma-separated): ").split(',')))
    
    
    capacity = int(input("Enter the maximum capacity of the knapsack: "))
    
   
    max_value = knapsack(profit, weights, capacity)
    print(f"The maximum profit in the knapsack is: {max_value}")


if __name__ == "__main__":
    main()
