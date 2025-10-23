
class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.insert(0, value)

    def pop(self):
        if len(self.stack) == 0:
            return "empty stack"
        else:
            return self.stack.pop(0)

    def peek(self):
        if len(self.stack) == 0:
            return "empty stack"
        else:
            return self.stack[0]
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.stack)