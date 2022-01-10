ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def sockMerchant(ar):
    pair = 0
    dictionary = {}
    for sock_colour in ar:
        if sock_colour in dictionary.keys():
            dictionary[sock_colour] += 1
            continue
        dictionary[sock_colour] = 1

    values = list(dictionary.values())

    for i in range(len(dictionary)):
        pair += values[i] // 2

    print(pair)


sockMerchant(ar)
