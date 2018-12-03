class queue:
    
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return str(self.queue)

    def enqueue(self, e):
        self.queue.append(e)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            temp = self.queue[0] 
            self.queue.pop(0)
            return temp


class BinaryNode:
    def __init__(self,element=None,left=None,right=None):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self,nspaces=0):
        s1 = ''
        if self.right:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = ' '*nspaces + str(self.element) + '\n'
        s3 = ''
        if self.left:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3 

    def size(self):
        s = 1
        if self.left:
            s += self.left.size()
        if self.right:
            s += self.right.size()
        return s

    def height(self):
        if self.left:
            hleft = self.left.height()
        else:
            hleft = -1
        if self.right:
            hright = self.right.height()
        else:
            hright = -1
        return 1 + max(hleft,hright)

    def search(self,e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def insert(self,e):
        parent = self
        current = None
        found = False
        
        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True
        
        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True
        
        if not found:
            if parent.element < e:
                parent.right = BinaryNode(e,None,None)
            else:
                parent.left = BinaryNode(e,None,None)
        
        return not found

    def max(self):
        if self.right != None:
            return self.right.max()
        else:
            return self.element

    def rsearch(self, e):
        if self.element == e:
            return self
        
        if self.element > e and self.left != None:
            return self.left.rsearch(e)

        if self.element < e and self.right != None:
            return self.right.rsearch(e)

        return False

    def rinsert(self, e, parent = None):
        if self.element < e:
            if self.right == None:
                self.right = BinaryNode(e)
                return True
            else:
                return self.right.rinsert(e, self)
        elif self.element > e:
            if self.left == None:
                self.left = BinaryNode(e)
                return True
            else:
                return self.left.rinsert(e, self)
        
        return False

    def showLevelOrder(self, queue):
        print('not done yet')
        #hier kom ok even niet uit. wat is die haat tegen recursie toch telkens?    

        
class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def height(self):
        if self.root:
            return self.root.height()
        else:
            return -1

    def insert(self,e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BinaryNode(e,None,None)
                return True
        return False

    def search(self,e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def max(self):
        return self.root.max()


    def rsearch(self, e):
        if self.root and e:
            return self.root.rsearch(e)
        else:
            return None

    def rinsert(self, e):
        return self.root.rinsert(e)

    def showLevelOrder(self):
        queue = queue()
        queue.enqueue(self.root)
        self.root.showLevelOrder(queue)
            
        

def make_node(a):
    if not a:
        return None
    if len(a) == 1:
        return BinaryNode(a[0],None,None)
    mid = len(a)//2
    left_node = make_node(a[:mid])
    right_node = make_node(a[mid+1:])
    return BinaryNode(a[mid],left_node,right_node)

def make_tree(a):
    root = make_node(a)
    return BinaryTree(root)


array = [x for x in range(16)]
tree = make_tree(array)

print(tree.max())

print(tree.rsearch(9))
print(tree.rsearch(20))
print(tree.rinsert(20))


print(tree)
