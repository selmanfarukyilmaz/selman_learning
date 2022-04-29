
def stair(n):
    line = ""
    for i in range(n+1):
        if i == 0:
            continue
        line = " " * (n-i)
        line = line + ("#" * i)
        print(line)

stair(19)


