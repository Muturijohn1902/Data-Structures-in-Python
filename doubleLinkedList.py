# A Single instance of how each Node will look like
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

# Class adding and linking new nodes
class doubleLinkedList:
    def __init__(self, data): #Declear a new class
        self.head = Node(data)
    # Add a list
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node.previous = current
            current.next = new_node

    #printing the Data in list
    def display(self, method = "asc"):
        if method.lower() == "asc":
            current = self.head
            while current:
                print(f">>{current.data}")
                current = current.next
            return
        if method.lower() == "desc":
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(f">>{current.data}")
                current = current.previous
    #Remove a node from the list
    def delete_node(self, target):
        current = self.head
        while current:
            if current.data == target:
                prev = current.previous
                nxt = current.next
                if prev == None:
                    current.data = nxt.data
                    current.next = nxt.next
                    nxt.next.previous = current
                elif nxt == None:
                    prev.next = None
                else:
                    prev.next = nxt
                    nxt.previous = prev
                print(f"{target} deleted")
            current = current.next
                
# Initiate a list the head will have 0 value
list = doubleLinkedList(0)
def add_data():
    data = input("add data: ")
    list.add_node(data)

# print the list
def display_list():
    print("use :acs for ascending or :desc for descending")
    order = input("--: ")
    list.display(order)

# remove the data from list
def delete_data():
    target = input("Enter target : ")
    list.delete_node(target)

isRunning = True
while isRunning:
    print("Menu")
    print("0. exit")
    print("1. add data")
    print("2. print list")
    print("3. delete node")
    choice = input("--: ")
    try:
        choice = int(choice)
    except ValueError:
        print("use :0 ,1 or 2")
    match(choice):
        case 0:
            isRunning = False
        case 1:
            add_data()
        case 2:
            display_list()
        case 3:
            delete_data()

