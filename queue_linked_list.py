class Node: #
    def __init__(self, data):
        self.data = data
        self.next = None

# Class adding and linking new nodes
class Queue:
    def __init__(self, data): #Declear a new class
        self.tail = None
    
    def enqueue(self, data):#add new data at the tail of the list
        if self.tail == None:
            self.tail = Node(data)
            return
        
        tail = self.tail #replace the tail data with the new data
        new_node = Node(tail.data)
        tail.data = data
        
        new_node.next = tail.next
        tail.next = new_node

        temp = tail
        while temp.next != None:
            temp = temp.next
        self.head = temp #set the first node as head

    def dequeue(self):# return and remove the head
        if self.tail.next == None:
            return "Empty list"
        
        head = self.head
        temp = self.tail
        while temp.next != head:
            temp = temp.next
        temp.next = None
        self.head = temp

        return head.data
        
    def peek(self): # return the head 
        if self.tail.next == None:
            return "Empty list"
        
        return self.head.data
    
    def size(self): # count and return the size of the list
        size = 0
        temp = self.tail
        while temp != None:
            size += 1
            temp = temp.next
        return size