def calculator(value: float, sec_value: float, step: int, operator: str) -> float:

    """
    Calculator without loop.
    :params:
                  value(float): The mein value of mathematical operation.
                  sec_value(float): The value that will be used in the operation that we will apply to the main value.
                  step(int): Number of repetitions of the math operation.
                  operator(str): Symbol of the mathematical operation to be applied.
    :return:
                  float: The result of the mathematical operation
    """

    if step == 0:
        return value
    else:
        if operator == "-":
            value = value - sec_value
            return calculator(value, sec_value, step - 1, operator)
        elif operator == "+":
            value = value + sec_value
            return calculator(value, sec_value, step - 1, operator)
        elif operator == "*":
            value = value * sec_value
            return calculator(value, sec_value, step - 1, operator)
        elif operator == "/":
            value = value / sec_value
            return calculator(value, sec_value, step - 1, operator)


print(calculator(calculator(5, 20, 2, "/")))

assert (calculator(500, 20, 3, "-")) == 440
assert (calculator(20, 20, 3, "+")) == 80
assert (calculator(100, 3, 4, "*")) == 8100
assert (calculator(5, 20, 2, "/")) == 0.0125
assert (calculator(0, 20, 3, "-")) == -60
