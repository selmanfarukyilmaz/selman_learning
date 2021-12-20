def fibonacci(step_size):
    fib = []
    a = 0
    b = 1
    if step_size > 2:
        fib.append(a)
        fib.append(b)
    if step_size == 1:
        fib.append(a)
        return fib

    if step_size == 2:
        fib.append(a)
        fib.append(b)
        return fib
#   a + b = a
#   a + b = b
#   a + b = a
#   a + b = b
    for step in range(step_size-2):

        if step % 2 == 0:
            a = a + b
            fib.append(a)
            continue
        b = a + b
        fib.append(b)

    return fib



print(fibonacci(100))






