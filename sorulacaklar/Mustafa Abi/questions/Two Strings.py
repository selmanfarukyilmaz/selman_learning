## ortak pairs_value kadar harf varsa yes or no !

def two_string(s1, s2, pairs_value):
    counter = 0
    for i in s1:
        if i in s2:
            counter += 1
    if counter >= pairs_value:
        print("Yes")
    else:
        print("NO")


two_string(s1="aaada", s2="ddaad", pairs_value=1)
two_string(s1="hi", s2="world", pairs_value=2)




def two_string(s1, s2):
    result = ""
    for i in s1:
        if i in s2:
            result = "Yes"
            break
        result = "No"
    print(result)




two_string(s1="asd", s2="ghaj")
two_string(s1="hi", s2="world")





