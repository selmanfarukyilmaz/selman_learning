class Record:

    def __init__(self, name, number):
        self.name = name
        self.number = number


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


r1 = Record(name="selman", number="541")
r2 = Record(name="mustafa", number="542")
r3 = Record(name="fatih", number="543")
r1_node = Node(data=r1)
r2_node = Node(data=r2)
r3_node = Node(data=r3)
phone_book = LinkedList()
phone_book.head = r1_node
r1_node.next = r2_node
r2_node.next = r3_node


def printList():
    temp = phone_book.head
    while temp:
        print(f"name: {temp.data.name} ---> number: {temp.data.number}")
        temp = temp.next


def add(name, number):
    phone_book_dic = {}
    temp = phone_book.head
    while temp:
        phone_book_dic[temp.data.name] = temp.data.number
        temp = temp.next

    if name in phone_book_dic.keys():
        print(f"The name {name} is already in the phone book.\nPlease try again.")
        return
    elif number in phone_book_dic.values():
        print(f"The number {number} is already in the phone book. Please try again.")
        return

    r_new = Record(name, number)
    new_node = Node(data=r_new)
    new_node.next = phone_book.head
    phone_book.head = new_node



