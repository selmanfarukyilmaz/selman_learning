arr = [15, 18, 19, 33, 2, 12]
n = len(arr)


def countRotations(arr, n):
    min = arr[0]

    for i in range(n):
        if min > i:
            min = arr[i]
            number_of_rotation = i

    return number_of_rotation


print(countRotations(arr, n))

# Input : arr[] = {15, 18, 2, 3, 6, 12}
# Output: 2
# Explanation : Initial array must be {2, 3,
# 6, 12, 15, 18}. We get the given array after
# rotating the initial array twice.
#
# Input : arr[] = {7, 9, 11, 12, 5}
# Output: 4
#
# Input: arr[] = {7, 9, 11, 12, 15};
# Output: 0
