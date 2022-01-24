
arr = [1, 3, 5, 2, 4, 6, 7]    #3

def minimumSwaps(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] == i+1:
            continue

        else:
            for ii in range(len(arr)):
                if arr[ii] == i+1:
                    arr[i], arr[ii] = arr[ii], arr[i]
                    result += 1
                    continue
    return result
minimumSwaps(arr)


