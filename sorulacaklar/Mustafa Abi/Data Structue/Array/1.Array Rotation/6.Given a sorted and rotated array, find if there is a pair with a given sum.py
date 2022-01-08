def fx(arr, expected_sum):
    arr_len = len(arr)
    for ix_a in range(arr_len):
        for ix_b in range(arr_len):
            if ix_a != ix_b and arr[ix_a] + arr[ix_b] == expected_sum:
                return True
    return False


assert fx(arr=[6, 8, 9, 10, 11, 15], expected_sum=23)
assert fx(arr=[6, 8, 9, 10, 11, 15], expected_sum=14)
assert fx(arr=[6, 8, 9, 10, 11, 15], expected_sum=17)
assert fx(arr=[6, 8, 9, 10, 11, 15], expected_sum=21)
assert not fx(arr=[6, 8, 9, 10, 11, 15], expected_sum=99)
assert not fx(arr=[6, 8, 9, 10, 11, 15], expected_sum=12)
assert not fx(arr=[6, 8, 9, 10, 11, 15], expected_sum=22)

assert fx(arr=[6, 8, 9, 11, 8, 11], expected_sum=22)
