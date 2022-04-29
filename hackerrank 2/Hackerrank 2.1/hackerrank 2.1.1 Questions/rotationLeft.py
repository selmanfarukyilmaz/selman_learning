n = 5
a = 4
d = [1, 2, 3, 4, 5]
# 5 1 2 3 4
x = 20
y = 10
z = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]


def rotLeft(n, a, d):
    left_rotation = a % n
    print(left_rotation)
    print(d[left_rotation:] + d[:left_rotation])


rotLeft(n, a, d)
rotLeft(x, y, z)