def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    if n <= 0:
        return []
    fib = [0]
    if n == 1:
        return fib
    fib.append(1)
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib