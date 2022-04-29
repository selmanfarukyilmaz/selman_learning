def minion_game(string):
    vowels =['A','E','I','O','U']
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string)-i
        else:
            stuart +=len(string)-i


    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")


minion_game("Banana")