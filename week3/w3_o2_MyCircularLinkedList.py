class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail
        if current != None:
            current = current.next
            s = s + str(current)
            if current != current.next:
                current = current.next
            else:
                return s
                
        while current != None:
            s = s + " -> " + str(current)
            current = current.next
            if(current == self.tail.next):
                break
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self,e):
        if not self.tail: # self.tail == None:
            self.tail = ListNode(e,None)
            self.tail.next = self.tail
        else:
            n = ListNode(e,self.tail.next)
            self.tail.next = n
            self.tail = self.tail.next
    
    def delete(self,e): 

        print('delete', e) # delete print

        if self.tail: # self.tail != None:
            current = self.tail
            while current.next != None and current.next.data != e:
                current = current.next
            if(current.next != None and current != current.next):
                if current.next == self.tail:
                    self.tail = current
                if current.next != None:
                    current.next = current.next.next
                if current.next == None:
                    self.tail = current
            else:
                self.tail = None

mylist = MyLinkedList()
print(mylist)
mylist.addLast(1)
mylist.addLast(2)
mylist.addLast(3)
mylist.addLast(4)
mylist.addLast(5)
print(mylist)
mylist.delete(3)
print(mylist)
mylist.delete(1)
print(mylist)
mylist.delete(5)
print(mylist)
mylist.delete(4)
print(mylist)
mylist.delete(2)
print(mylist)