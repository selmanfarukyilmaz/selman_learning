
def minimumBribes(q):
    n = len(q)
    result = ""
    counter = 0
    for i in range(n):
        if q[i] - (i + 1) >= 2:
            result = "Too chaotic"

        if q[i] < (i + 1):
            counter += (i + 1) - q[i]
    print(counter)
    print(result)


minimumBribes([2, 5, 1, 3, 4])





def minimumBribes(q):
    result = ""
    counter = 0
    for i in range(n):
        if q[i] - (i + 1) >= 3:
            result = "Too chaotic"

        if q[i] < (i + 1):
            counter += (i + 1) - q[i]
    print(counter)
    if result != "":
        print(result)








