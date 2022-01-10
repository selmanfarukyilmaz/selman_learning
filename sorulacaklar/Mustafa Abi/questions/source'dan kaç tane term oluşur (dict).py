from collections import Counter


def term_source(source, term):
    source = (Counter(source))
    term = Counter(term)
    counter = 999
    for i in term:
        divide = source[i] // term[i]
        if divide < counter:
            counter = divide

    return counter


assert term_source("abcbaccab", "abc") == 3
assert term_source("aaaa", "a") == 4
assert term_source("3131", "31") == 2
assert term_source("xxdd", "xxd") == 1
assert term_source("sssseeeeell", "sell") == 1
