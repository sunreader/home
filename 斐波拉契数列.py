def fib(max):
    n, a, b = 0, 0, 1
    while b < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(100), fib(5000))
