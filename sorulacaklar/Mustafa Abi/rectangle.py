

def rectangle(height=6, length=10, thickness=2):
    a = ""
    for i in range(thickness):
        hashtag_top = "#" * length
        print(hashtag_top)
        a = a + hashtag_top + "\n"

    for i in range(thickness):
        space_len = length - (2*thickness)
        space = " " * space_len
        hashtag_midle = "#" * thickness
        print(hashtag_midle + space + hashtag_midle)

    print(a)


rectangle()


