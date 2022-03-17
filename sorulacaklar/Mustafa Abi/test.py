a = {"x":1}

a["x"] = 2
print(a)


from collections import defaultdict

d = defaultdict(list)

d["selman"].add(1)
d["selman"].add(2)


print(d)

from collections import defaultdict

n, m = map(int, input().split())

a = defaultdict(list)

for i in range(n):
    a[input()].append(i + 1)

for i in range(m):
    inp = input()
    if inp in a:
        print(" ".map(str, join(a[inp])))

    else:
        print(-1)
