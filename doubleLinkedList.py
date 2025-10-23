
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class doubleLinkedList:
    def __init__(self, data):
        self.head = Node(data)

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
                
            
   
dll = doubleLinkedList(10)
dll.add_node(10)
dll.add_node(20)
dll.add_node(30)

print("Ascending:")
dll.display("asc")

print("Descending:")
dll.display("desc")
