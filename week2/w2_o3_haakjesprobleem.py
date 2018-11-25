class mysrack:
    stack = []
    pointer = 0

    """
    description
    this function checks if the stack is empty

    """

    def isEmpty(self):
        if (self.pointer == 0):
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
        if (not self.isEmpty()):
            return self.stack[self.pointer - 1]
        return None

    """
    description
    this function pops the last item that was pushed to the stack

    """

    def pop(self):
        if (not self.isEmpty()):
            self.stack.pop(self.pointer - 1)
            self.pointer -= 1


"""
description
return the opposite bracket

parameter
------
bracket : string
    this is the bracket you want the opposite from

return
------
bracket : string
    this is the opposite bracket of the one given as parameter

"""
def getReversedBracket(bracket):
    parentheses = {
        "{": "}",
        "}": "{",
        "[": "]",
        "]": "[",
        "<": ">",
        ">": "<",
        "(": ")",
        ")": "("
    }
    return parentheses[bracket]

"""
description
this function checks if parentheses are nested correctly

parameter
------
string : string
    this is the string to look in

return
------
 : bool
    if the string has correctly nested parentheses than the result is True otherwise it will return False

"""
def nestedCorrectCheck(string):
    stack = mysrack()
    for i in string:
        if(i == '{' or i == '[' or i == '(' or i == '<'):
            stack.push(i)
        if(i == '}' or i == ']' or i == ')' or i == '>'):
            if(stack.peek() == getReversedBracket(i)):
                stack.pop()
                continue
            return False
    return True

print(nestedCorrectCheck("[()]"))
print(nestedCorrectCheck("[(])"))