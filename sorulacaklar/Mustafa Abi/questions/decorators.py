import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"The function completed in {end - start} seconds.")
        return result
    return wrapper


@decorator
def square(a_list):
    time.sleep(1)
    result = []
    for i in a_list:
        result.append(i * i)
    return result


print(square([1, 2, 3, 4]))
