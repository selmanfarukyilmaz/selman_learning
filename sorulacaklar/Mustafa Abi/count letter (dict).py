import pprint

letters = "selman","mustafa","fatih","kadir","süleyman"


for letter in letters:
    dictionary = {}

    for word in letter:
        if word in dictionary:
            dictionary[word] += 1
            continue
        dictionary[word] = 1

    pprint.pprint(dictionary)



