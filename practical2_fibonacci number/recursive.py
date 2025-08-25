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