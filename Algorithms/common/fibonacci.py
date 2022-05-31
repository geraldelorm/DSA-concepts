# Recursive
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Time Complexity = O(2^n)
# Space Complexity = O(n)


# Recursive - with memoization
def fib(n, memo = {0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# Time Complexity = O(nlogn)
# Space Complexity = O(n)


# Iterative 
def fib(n):
    arr = [0, 1, 1]
    for i in range(2, n):
        arr.append(arr[-1] + arr[-2])
    return arr[n]

# Time Complexity = O(n)
# Space Complexity = O(n)
