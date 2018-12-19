import random

class sc_hashing:

    def __init__(self, length):
        self.ht = []
        for i in range(200):
            self.ht.append(set())
        self.htLength = length

    def __repr__(self):
        return str(self.ht)

    def find(self, e):
        index = e%self.htLength

        if self.ht[index] != set():
            for item in self.ht[index]:
                if item == e:
                    return index
        return False

    def search(self, e):
        if self.find(e) != False:
            return True

    def thFullCheck(self):
        count = 0
        for item in self.ht:
            if item != set():
                count += 1
        if count / self.htLength >= 0.75:
            return True

        return False

    def insert(self, e):        
        index = e % self.htLength
        try:
            self.ht[index].add(e)
        except:
            return False

        if self.thFullCheck():
            self.rehash(self.htLength*2)

        return True

    def delete(self, e):
        index = self.find(e)
        if index != False:
            self.ht[index].remove(e)
            return True
        return False
        

    def rehash(self, new_len):
        temp = sc_hashing(new_len)
        for items in self.ht:
            if items != set():
                for item in items:
                    temp.insert(item)
        self.htLength = temp.htLength
        self.ht = temp.ht

        print("\nrehash")
        print(self.htLength, self.ht)

sc_hash = sc_hashing(100)
for i in range(200):
    sc_hash.insert(random.randint(1, 400))
    # sc_hash.insert(random.uniform(0,1))

for i in range(100):
    sc_hash.delete(random.randint(1, 400))
    # sc_hash.delete(random.uniform(0,1))

print("\nDone:")
print(sc_hash)