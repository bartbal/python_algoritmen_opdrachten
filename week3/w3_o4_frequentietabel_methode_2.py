from typing import Tuple


class TrieNode(object):
    
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1
    

def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0

    return True, node.counter


def getFrequentie(fileName):
    trie = TrieNode('*')
    f=open(fileName, 'r')
    if f.mode == 'r':
        contents = f.readlines()
        for line in contents:
            word = ''
            for letter in line:
                if letter.isalpha():
                    word += letter
                elif word != '':
                    add(trie, word)
    print(find_prefix(trie, 's'))                        
getFrequentie('tekst')

#nog niet af. ga denk ik een eigen trie class maken maar dat lukt niet meer voor de deadline