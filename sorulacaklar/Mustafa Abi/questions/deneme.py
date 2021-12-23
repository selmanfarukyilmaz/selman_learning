

import string
alpha = string.ascii_lowercase



def ragnoli(n = 20):
    count = (n-1) * 4 + 1
    print(count)
    middle_line = alpha[:n]
    middle_line = middle_line[::-1] + middle_line[1:n]
    middle_line = "-".join(middle_line)
    middle_len = len(middle_line)
    print(middle_len)
    print(middle_line)

    for i in reversed(range(n)):
        line = middle_line[2*i:middle_len - i*2]
        line = line.center(middle_len,"-")
        print(line)

    for i in (range(1,n)):
        line = middle_line[2*i:middle_len - i*2]
        line = line.center(middle_len, "-")
        print(line)



ragnoli()



#
# a = "a-b-c-d-e"
# print(a[4:5])
# print(a[2:7])
# print(a[0:9])
#


#size 3 9

# ----c----         2   a - 2 * n                  5:6
# --c-b-c--         1                              3:8
# c-b-a-b-c   5     0
# --c-b-c--         1
# ----c----         2

#size 4 13

#size 5 17

# --------e--------   4
# ------e-d-e------   3
# ----e-d-c-d-e----   2
# --e-d-c-b-c-d-e--   1
# e-d-c-b-a-b-c-d-e   0
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


