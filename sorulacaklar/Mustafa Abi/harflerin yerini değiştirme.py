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
















    # a = 3
    # b = 5
    # print(f"a: {a} - b: {b}")  # prints "a: 3 - b: 5"
    # # do something here
    # print(f"a: {a} - b: {b}")  # prints "a: 5 - b: 3"