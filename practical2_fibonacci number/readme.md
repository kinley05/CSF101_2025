# iterative implementation
def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input"
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    a, b = 0, 1
    for i in range(3, n+1):
        a, b = b, a + b

    return b

print(f"Iterative: {fibonacci_iterative(10)}")

"""
Calculate the nth Fibonacci number using iteration.
    
Args:
    n (int): The position in the Fibonacci sequence (n >= 1)
    
Returns:
    int: The nth Fibonacci number
"""

#recursive im plementation
def fibonacci_recursive(n):
    if n <= 0:
        return "invalid input"
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(f"Rescursive: {fibonacci_recursive(10)}")

"""
Calculate the nth Fibonacci number using recursion.
    
Args:
    n (int): The position in the Fibonacci sequence (n >= 1)
    
Returns:
    int: The nth Fibonacci number
"""