def factorial_recursive(n):
    """Calculate factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
    
if __name__ == "__main__":
    print(factorial_recursive(5))  