class Node: # a single instance of each node
    def __init__(self, data):
        self.data = data
        self.next = None

# a class tha t will create a tail node and data
class Queue:
    def __init__(self, data): #Declear a new class
        self.tail = Node(data)
    
    def enqueue(self, data): #add data to the tail
        tail = self.tail
        new_node = Node(tail.data)
        tail.data = data
        
        new_node.next = tail.next
        tail.next = new_node

        temp = tail
        while temp.next != None:
            temp = temp.next
        self.head = temp

    def dequeue(self): # retrive and delete the data on top/ head
        if self.tail.next == None:
            return "Empty list"
        
        head = self.head
        temp = self.tail
        while temp.next != head:
            temp = temp.next
        temp.next = None
        self.head = temp

        return head.data
        
    def peek(self): # retrieve the data on top/head
        if self.tail.next == None:
            return "Empty list"
        
        return self.head.data
    
    def size(self):# check the size of list
        size = 0
        temp = self.tail
        while temp != None:
            size += 1
            temp = temp.next

        return size
    
