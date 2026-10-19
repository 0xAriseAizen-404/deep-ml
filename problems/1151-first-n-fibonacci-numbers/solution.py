def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    if n <= 0:
        return []
    fibs = [0]
    if n == 1:
        return fibs
    fibs.append(1)
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs