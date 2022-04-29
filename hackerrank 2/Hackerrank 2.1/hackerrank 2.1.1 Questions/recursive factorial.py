def factorial(value: int) -> int:
    """

    :param value: Factorial value.
    :return:  Result of factorial.
    """
    if value == 1:
        return value
    else:
        return value * factorial(value - 1)


assert factorial(9) == 362880
assert factorial(8) == 40320
assert factorial(7) == 5040
assert factorial(6) == 720
assert factorial(5) == 120
assert factorial(4) == 24
assert factorial(3) == 6
assert factorial(2) == 2
assert factorial(1) == 1
