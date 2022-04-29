
number = 13
a = []
while number >= 2:
    a.append(number % 2)
    number = number // 2
a.append(number)

counter = 0
counter2 = 1
listem = []

x = len(a)
for i in range(x-1):
    if a[i] and a[i + 1] == 1:
        counter2 += 1
        listem.append(counter2)
        continue

    counter2 = 1

if len(listem) == 0:
    print(1)


else:
    print(max(listem))




num = 13

result = 0
maximum = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0

    num //= 2

print(maximum)


