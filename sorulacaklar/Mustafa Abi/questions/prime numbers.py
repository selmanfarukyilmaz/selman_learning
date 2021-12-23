x = (int(input()) + 1)
a = []


for i in range(2, x):
    for b in range(2, i):   # 2 3
        if i % b == 0:
            break
    else:
        a.append(i)
print(a)

