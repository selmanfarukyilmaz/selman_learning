def is_prime(check_is_prime):
    if check_is_prime <= 1:
        return False
    elif check_is_prime == 2:
        return True

    else:
        final = False
        for i in range(2,check_is_prime):
            if check_is_prime % i == 0:
                final = False
                break
            else:
                final = True
        return final




print(is_prime(check_is_prime=int(input())))