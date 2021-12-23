arr = [1, 2, 3, 4, 5,7]
n = len(arr)


def rotate(arr, n):
    last = arr[n - 1]
    arr.pop()
    arr.insert(0, last)
    print(arr)


rotate(arr, n)
