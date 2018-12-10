class trieNode:
    def __init__(self, name):
        self.children = {}
        self.name = name
        self.occurrences = 0
    
    def toFile(self, file, s = ''):
        for key in self.children:
            self.children[key].toFile(file, s + self.name)

        line = s + self.name + ':' + str(self.occurrences) + '\n'
        file.write(line)

    def print(self, s = ''):
        for key in self.children:
            self.children[key].print(s + self.name)

        print(s + self.name, self.occurrences)

            
    def insert(self, word):
        if(word == ''):
            return
        found = False
        for key in self.children:
            if(key == word[0]):
                found = True
                self.children[key].occurrences += 1
                self.children[key].insert(word[1:])
        if(not found):
            self.children[word[0]] = trieNode(word[0])
            self.insert(word)
        return
        


class trie:
    def __init__(self):
        self.root = trieNode('')
    
    def insert(self, word):
        self.root.insert(word)

    def print(self):
        self.root.print()

    def toFile(self, filename):
        file = open(filename,'w')
        self.root.toFile(file)


tree = trie()
tree.insert('hallo')
tree.insert('hallo')
tree.insert('hoi')
tree.insert('haaaa')
tree.insert('haa')
tree.insert('pfffff')
tree.insert('halen')
tree.print()

tree.toFile('result2')