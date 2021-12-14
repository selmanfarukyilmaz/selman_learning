def print_rangoli(size):
    n = (2 * size) - 1
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
                ]

    alphabet_size = alphabet[:size]
    a = alphabet_size[::-1] + alphabet_size[1:size]
    middle_line_in_regnolli = ""

    for i in a:
        middle_line_in_regnolli += i + "-"
        
    l = len(middle_line_in_regnolli)
    
    # h-g-f-e-d-c-b-a-b-c-d-e-f-g-h- 'nin sonundaki kısa çizgiyi çıkartma işlemi.
    st2 = middle_line_in_regnolli[:l - 1]
    lenglth_of_middle_line_in_regnolli = len(st2)
    reverse = alphabet_size[::-1]


    for i in range(len(reverse)):
        line_variable = ""
        counter = 0
        for k in range(i + 1):
            counter += 1
            line_variable += reverse[counter-1] + "-"
        for k in range(i + 1):
            counter -= 1
            if k > 0:
                line_variable += reverse[counter] + "-"
        line_variable = line_variable[:-1]
        line_variable = line_variable.center(lenglth_of_middle_line_in_regnolli, "-")
        print(line_variable)

    for i in range(len(reverse)-1):
        line_variable = ""
        counter = 0
        for k in range(len(reverse)-i-1):
            counter += 1
            line_variable += reverse[counter - 1] + "-"
        for k in range(len(reverse)-i-1):
            counter -= 1
            if k > 0:
                line_variable += reverse[counter] + "-"
        line_variable = line_variable[:-1]
        line_variable = line_variable.center(lenglth_of_middle_line_in_regnolli, "-")
        print(line_variable)


print_rangoli(8)
