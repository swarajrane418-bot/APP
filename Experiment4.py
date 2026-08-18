

def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {}

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

   
    if n in memo:
        return memo[n]

    # Calculate and store result
    memo[n] = (fibonacci_memoization(n - 1, memo) +
               fibonacci_memoization(n - 2, memo))

    return memo[n]




def fibonacci_tabulation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Create table
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

  
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]





n = int(input("Enter the value of n: "))

print("\nFibonacci using Memoization:")
print("Fibonacci(", n, ") =", fibonacci_memoization(n))

print("\nFibonacci using Tabulation:")
print("Fibonacci(", n, ") =", fibonacci_tabulation(n))