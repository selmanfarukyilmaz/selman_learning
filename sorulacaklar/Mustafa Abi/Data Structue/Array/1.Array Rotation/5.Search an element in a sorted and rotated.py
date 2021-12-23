arr = {5, 6, 7, 8, 9, 10, 1, 2, 3,4,11}


def x (arr,key):
    lengh = len(arr)
    mid_index = lengh // 2

    arr_list = list(arr)

    if key <= mid_index:
        left = arr_list[:mid_index]
        for i in left:
            if key == i:
                print(i-1)
                break

    if key > mid_index:
        right = arr_list[mid_index:]
        for i in right:
            if key ==i:
                print(i-1)
                break

x(arr,1)
x(arr,2)
x(arr,3)
x(arr,4)
x(arr,6)
x(arr,7)
x(arr,8)
x(arr,9)
x(arr,10)
x(arr,11)





