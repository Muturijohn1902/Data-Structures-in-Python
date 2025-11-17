#A simple queue using python list
class queue:
    def __init__(self):
        self.queue = []
    
    def enqueu(self, value):# add an element at the bottom/end of the queue
        self.queue.append(value)

    def dequeue(self):#return and remove the first element of the queue
        if len(self.queue) == 0:
            return "empty queue"
        else:
            return self.queue.pop(0)
        
    def peek(self):# return the first element of the queue
        if len(self.queue) == 0:
            return "empty queue"
        else:
            return self.queue[0]
        
    def isEmpty(self):#return true if the list is empty
        if len(self.queue) == 0:
            return True
        else:
            return False
        
    def size(self):#The size of the queue
        return len(self.queue)
    
