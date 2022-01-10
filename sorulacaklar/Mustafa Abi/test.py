import time


def foo():
    for i in range(9999):
        print("selman")
    return


start_time = time.time()
foo()
elapsed_time = time.time() - start_time
print(elapsed_time)
