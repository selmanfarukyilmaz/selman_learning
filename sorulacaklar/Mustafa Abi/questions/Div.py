
def div(start=30, stop=45, divider=5):
    start_stop = []
    divisibles = []

    for i in range(start, stop+1):
        start_stop.append(i)
    print(start_stop)

    for i in range(len(start_stop)):
        if start_stop[i] % divider == 0:
            divisibles.append(start_stop[i])
    return divisibles
        

print(div())


x = 1
y = 2
print(x,y)
x,y = y,x

print(x,y)