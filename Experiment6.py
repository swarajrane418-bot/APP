

def knapsack_top_down(weights, profits, capacity, n, dp):

    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # If value is already calculated
    if dp[n][capacity] != -1:
        return dp[n][capacity]

    # If item does not fit
    if weights[n - 1] > capacity:

        dp[n][capacity] = knapsack_top_down(
            weights, profits, capacity, n - 1, dp
        )

    else:

        # Include item
        include = profits[n - 1] + knapsack_top_down(
            weights,
            profits,
            capacity - weights[n - 1],
            n - 1,
            dp
        )

        # Exclude item
        exclude = knapsack_top_down(
            weights,
            profits,
            capacity,
            n - 1,
            dp
        )

        # Maximum profit
        dp[n][capacity] = max(include, exclude)

    return dp[n][capacity]




def knapsack_bottom_up(weights, profits, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Process each item
    for i in range(1, n + 1):

        # Process each capacity
        for w in range(1, capacity + 1):

            # If item fits
            if weights[i - 1] <= w:

                # Include item
                include = profits[i - 1] + \
                          dp[i - 1][w - weights[i - 1]]

                # Exclude item
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:

                # Item does not fit
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]




weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

n = len(weights)




dp = [[-1 for _ in range(capacity + 1)]
      for _ in range(n + 1)]

top_down_result = knapsack_top_down(
    weights, profits, capacity, n, dp
)




bottom_up_result = knapsack_bottom_up(
    weights, profits, capacity
)




print("Weights  :", weights)
print("Profits  :", profits)
print("Capacity :", capacity)

print("\nTop-Down Maximum Profit  =", top_down_result)
print("Bottom-Up Maximum Profit =", bottom_up_result)