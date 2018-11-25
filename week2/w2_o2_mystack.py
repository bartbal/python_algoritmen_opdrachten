class mysrack:
    stack = []
    pointer = 0

    """
    description
    this function checks if the stack is empty
    
    """
    def isEmpty(self):
        if(self.pointer == 0):
            return True
        return False

    """
    description
    this function pushes an item to the top of the stack

    parameter
    ------
    item : 
        item to add to the stack

    """
    def push(self, item):
       self.stack.append(item)
       self.pointer += 1

    """
    description
    this function return the last item that was pushed to the stack

    return
    ------
    item
        last item that was pushed to the stack
        

    """
    def peek(self):
        if(not self.isEmpty()):
            return self.stack[self.pointer-1]
        return None

    """
    description
    this function pops the last item that was pushed to the stack

    """
    def pop(self):
        if (not self.isEmpty()):
            self.stack.pop(self.pointer-1)
            self.pointer -= 1

stack = mysrack()
stack.push('hello1')
stack.push('hello2')
stack.push('hello3')
stack.push('hello4')
stack.push('hello5')
print(stack.isEmpty())
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.isEmpty())
