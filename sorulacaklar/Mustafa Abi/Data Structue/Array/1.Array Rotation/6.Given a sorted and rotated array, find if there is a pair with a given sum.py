arr = [6, 8, 9, 10, 11, 15]
sum = 16


def fx(arr, sum):
    counter = 0
    sort_arr = sorted(arr)

    for i in sort_arr:
        sort_arr.pop(counter)
        counter += 1

        for ii in sort_arr:
            if i + ii == sum:
                return True

    return False


print(fx(arr, sum))
