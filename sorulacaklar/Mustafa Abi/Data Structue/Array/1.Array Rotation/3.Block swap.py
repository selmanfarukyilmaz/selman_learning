arr = [1, 2, 3, 4, 5, 6, 7];
d = 3
n = len(arr)


def block_swap(arr, d, n):
    append_list = []
    for i in arr:

        if i <= d:
            append_list.append(i)
    arr_sliced = arr[d:]

    for i in append_list:
        arr_sliced.append(i)
    print(arr_sliced)


block_swap(arr, d, n)

