a = [1, 1, 1, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     1, 1, 1, 0, 0, 0,
     0, 0, 2, 4, 4, 0,
     0, 0, 0, 2, 0, 0,
     0, 0, 1, 2, 4, 0]

b = [1, 1, 1, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     1, 1, 1, 0, 0, 0,
     0, 9, 2, -4, -4, 0,
     0, 0, 0, -2, 0, 0,
     0, 0, -1, -2, -4, 0]


def hourglassSum(arr):
    my_list = []

    x = -3
    for i in range(4):
        x += 2
        for ii in range(4):
            x += 1
            my_list.append(arr[0 + x] + arr[1 + x] + arr[2 + x] + arr[7 + x] + arr[12 + x] + arr[13 + x] + arr[14 + x])

    return max(my_list)


assert (hourglassSum(b)) == 13
assert (hourglassSum(a)) == 19