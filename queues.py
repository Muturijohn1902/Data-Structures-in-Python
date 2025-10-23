
class queue:
    def __init__(self):
        self.queue = []
    
    def enqueu(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return "empty queue"
        else:
            return self.queue.pop(0)
        
    def peek(self):
        if len(self.queue) == 0:
            return "empty queue"
        else:
            return self.queue[0]
        
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.queue)
    
