cache = {}
def stepPerms(n):
    if n == 1:return 1
    if n == 2:return 2
    if n == 3:return 4
    if n not in cache:
        cache[n] = stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
    return cache[n]