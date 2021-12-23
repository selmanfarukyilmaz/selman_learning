source = "sdfsfsdssf"
term = "sdsfff"

total_letter_set = set(source+term)
letters = list(total_letter_set)
number_of_letters = len(letters)

letter_count_source = [0] * number_of_letters
letter_count_term = [0] * number_of_letters
x = [0] * number_of_letters


for i in source:
  for ix in range(number_of_letters):
    current_letter = letters[ix]
    if i == current_letter:
      letter_count_source[ix] = letter_count_source[ix]+1


for i in term:
  for ix in range(number_of_letters):
    current_letter_term = letters[ix]
    if i == current_letter_term:
      letter_count_term[ix] = letter_count_term[ix]+1


for ix in range(number_of_letters):
  x[ix] = letter_count_source[ix] // letter_count_term[ix]

print(letter_count_source)
print(letter_count_term)
print(x)
print(min(x))
# 2d 3f 5s
# 1d 3f 2s

# 2  1  2


