def rectangle(height=16, length=13, thickness=3):
    hashtag_top = "#" * length
    hashtag_top = (hashtag_top + "\n") * thickness
    print(hashtag_top[:-1])

    space_len = length - (2 * thickness)
    space = " " * space_len
    hashtag_midle = "#" * thickness
    midle_line = (hashtag_midle + space + hashtag_midle)
    midle_line = (midle_line + "\n") * (height - (2 * thickness))
    print(midle_line[:-1])

    print(hashtag_top[:-1])


rectangle()

a = 2
b = 3

a, b = b, b + a

print(a)
print(b)


