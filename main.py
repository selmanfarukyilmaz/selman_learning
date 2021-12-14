# x = (int(input()) + 1)
# a = []
#
# for i in range(2, x):
#     for b in range(2, i):   # 2 3
#         if i % b == 0:
#             break
#     else:
#         a.append(i)
# print(a)

def is_prime (check_is_prime):
    if 1 <check_is_prime <= 2:
        print("True")
        return
    elif check_is_prime <= 1:
        print("False")
        return
    for i in range(2,check_is_prime):
        if (check_is_prime)%i == 0:
            result = "False"
        else:
            result = "True"
        return print(result)
        break
is_prime(check_is_prime=int(input()))
