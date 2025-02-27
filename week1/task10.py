# Task 10: Write a Python program to print the first n terms of the Fibonacci sequence, where n is input from the user

# optimized approach
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

n = int(input("Enter a number: "))
print(f"Fib of {n} is: {fib(n, {})}")

