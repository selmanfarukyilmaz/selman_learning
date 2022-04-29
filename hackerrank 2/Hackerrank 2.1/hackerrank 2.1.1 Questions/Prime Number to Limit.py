
def prime_limit(limit):
    prime_list = []
    for i in range(2, prime_list):
        for b in range(2, i):
            if i % b == 0:
                break
        else:
            prime_list.append(i)
    print(prime_list)

prime_limit(5)