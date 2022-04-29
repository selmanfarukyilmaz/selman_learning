def superDigit(n, k=1):
    if int(n) < 10:
        return int(n)

    n = n * k

    total = 0
    for letter inn:
        total += int(letter)
    return superDigit(str(total))




def superDigit(n, k=1):
    if int(n) < 10:
        return (int(n))
    if k>1:
        n = n*k
    total = sum(map(int,list(n)))
    return superDigit(str(total))
(superDigit("123", 3))





def digitSum(n, k):
    x = sum(map(int, list(n)))
    if k == 1:
        return ds(x)
    else:
        return ds(x * k)

def ds(x):
    if x < 10:
        return x
    else:
        return ds(sum(map(int, list(str(x)))))
