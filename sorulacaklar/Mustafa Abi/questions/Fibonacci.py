def fibonacci(step_size):
    fib = [0, 1]
    if step_size < 3:
        return fib[:step_size]

    for step in range(2, step_size):
        new_element = fib[step - 2] + fib[step - 1]
        fib.append(new_element)

    return fib


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(30))


def fib(step_size):
    a = 0
    b = 1
    yield 0
    for i in range(1, step_size):
        a, b = b, a + b

        yield a


print(list(fib(5)))
