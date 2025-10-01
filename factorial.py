def factorial_tr(n: int) -> int:
    if n < 0:
        raise ValueError("The Fact blah blah blah is nt defined for negative numbers")
    return fact_tail(n, 1)
    
def fact_tail(n, acc=1):
    if n == 0:
        return acc
    else:
        return fact_tail(n - 1, n * acc)