# # n = int(input())
# # phones = {}
# # listbir = "sam 99912222"
# # iki = "sam"
# # for i in range(n):
# #     line = input()
# #     line = line.split()
# #     phones[line[0]] = line[1]
# #
# # for i in range(n):
# #     name = input()
# #     if name in phones.keys():
# #         print(f"{name}={phones.get(name)}")
# #     else:
# #         print("Not found")
# #
# #
# #
# # def factorial(n):
# #     a = 1
# #     for i in range(1,n+1):
# #         a = a * i
# #     print(a)
# #
# # #
# # # factorial(4)
# #
# # number = 5
# # a = []
# # while number >= 2:
# #     a.append(number % 2)
# #     number = number // 2
# # a.append(number)
# # counter = 0
# # counter2 = 1
# # listem = []
# # x = len(a)
# #
# # for i in range(x-1):
# #     if a[i] and a[i + 1] == 1:
# #         counter2 += 1
# #         listem.append(counter2)
# #     if a[i] and a[i + 1] != 1:
# #         counter2 = 1
# #
# # if (max(listem)) < 1:
# #     print(1)
# # else:
# #     print(max(listem))
# #
# #
# #
# # number = 13
# # a = []
# # while number >= 2:
# #     a.append(number % 2)
# #     number = number // 2
# # a.append(number)
# # counter = 0
# # counter2 = 1
# # listem = []
# # x = len(a)
# #
# # for i in range(x-1):
# #     if a[i] and a[i + 1] == 1:
# #         counter2 += 1
# #         listem.append(counter2)
# #     if a[i] and a[i + 1] != 1:
# #         counter2 = 1
# #
# # if len(listem) == 0:
# #     print(1)
# #
# #
# # else:
# #     print(max(listem))
# #
# #
# #
# #
# # num = 13
# #
# # result = 0
# # maximum = 0
# #
# # while num > 0:
# #     if num % 2 == 1:
# #         result += 1
# #         if result > maximum:
# #             maximum = result
# #
# #     else:
# #         result = 0
# #
# #     num //= 2
# #
# # print(maximum)
# #
# #
# #
# #
# #
# #
# #
# a = (1+2,3)
# print(type(a))
# print(a)




letters = "selman", "mustafa", "fatih", "kadir", "süleyman"

for letter in letters:
    dictionary = {}

    for word in letter:
        if word in dictionary:
            dictionary[word] += 1
            continue
        dictionary[word] = 1

    print(dictionary)


from collections import defaultdict

letters = "selman", "mustafa", "fatih", "kadir", "süleyman"

d = defaultdict(int)
for letter in letters:
    for k in letter:
        d[k] += 1

print(d.items())

