def fib(n, cache={}):
    if n in cache:
        return cache[n]

    if n == 0:
        cache[n] = 0
        return 0

    elif n == 1:
        cache[n] = 1
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(10) == 55
assert fib(15) == 610
