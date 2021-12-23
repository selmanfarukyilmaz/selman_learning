source = "sdfsfsdssf"
term = "sdsfff"


# find how many of each character in the source / output= # 2d 3f 5s
def find_count_of_each_character(input_string, characters):
    letter_count = [0] * len(characters)
    for i in input_string:
        for ix in range(len(characters)):
            current_letter = characters[ix]
            if i == current_letter:
                letter_count[ix] = letter_count[ix] + 1
    return letter_count


# find distinct/unique characters in inputs
total_letter_set = set(source + term)
# convert to list since set is not ordered and we need ordered letters
letters = list(total_letter_set)


letter_count_source = find_count_of_each_character(input_string=source, characters=letters)
letter_count_term = find_count_of_each_character(input_string=term, characters=letters)


letter_count_ratio = [0] * len(letters)


for index in range(len(letters)):
    letter_count_ratio[index] = letter_count_source[index] // letter_count_term[index]

print(letter_count_source)
print(letter_count_term)
print(letter_count_ratio)
print(min(letter_count_ratio))



# 2d 3f 5s
# 1d 3f 2s

# 2  1  2

# 1
