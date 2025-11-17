# A stack data structure using a python list
class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):# add new data
        self.stack.insert(0, value)

    def pop(self):#return and remove the top element
        if len(self.stack) == 0:
            return "empty stack"
        else:
            return self.stack.pop(0)

    def peek(self):#return the top element
        if len(self.stack) == 0:
            return "empty stack"
        else:
            return self.stack[0]
        
    def isEmpty(self):# Return true if the stack is empty
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def size(self):#return the size of the stack
        return len(self.stack)