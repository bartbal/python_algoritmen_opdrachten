class cArray:
    head = 0
    tail = 0
    size = 8
    array = []

    def __init__(self, size = 8):
        self.size = size

    def enque(self, item):
        self.array.append(item)

        self.tail = (self.tail + 1) % (len(self.array))

    def deque(self):
        temp = self.array[self.head]
        self.head = (self.tail + 1) % (len(self.array))

        return temp

