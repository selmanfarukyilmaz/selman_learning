a = [str(input("a değerinizi belirleyiniz: "))]
b = [str(input("b değerinizi belirleyiniz: "))]
c = [a] + [b]
stra = "".join(a)
strb = "".join(b)
for i in c:
   stri = "".join(i)
   if i == a:
       print((f"a: {stri} - b: {strb}"))

   if i == b:
       print((f"a: {stri} - b: {stra}"))





a = 5
b = 3
print((f"a: {a} - b: {b}"))

save = a
a = b
b = save

print((f"a: {a} - b: {b}"))


a = 1
b = 2
print((f"a: {a} - b: {b}"))

a = a * b  #2 = a
b = a / b  #1 = b
a = a / b  #2 = a

print((f"a: {a} - b: {b}"))














    # a = 3
    # b = 5
    # print(f"a: {a} - b: {b}")  # prints "a: 3 - b: 5"
    # # do something here
    # print(f"a: {a} - b: {b}")  # prints "a: 5 - b: 3"