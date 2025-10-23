
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, data):
        self.head = Node(data)

    def addNode(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def display(self):
        current = self.head
        while current:
            print(f">>{current.data}")
            current = current.next

dll = linkedList(10)
dll.addNode(10)
dll.addNode(20)
dll.addNode(30)

print("Ascending:")
dll.display()
