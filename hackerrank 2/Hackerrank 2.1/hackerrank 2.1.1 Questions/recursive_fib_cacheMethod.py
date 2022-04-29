memory = {}
def fibonacci(n):
    if n < 2:
        return n
    if not n in memory.keys():
        memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(10) == 55
assert fibonacci(15) == 610
