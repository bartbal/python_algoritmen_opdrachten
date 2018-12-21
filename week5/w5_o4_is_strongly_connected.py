import math
INFINITY = math.inf

class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)
    
    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)

class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self): # voor afdrukken
        return str(self.data) 

    def __lt__(self, other): # voor sorteren
        return self.data < other.data

def vertices(G):
    return sorted(G)

def edges(G):
    return [(u,v) for u in vertices(G) for v in G[u]]

def is_connected(G,s):
    V = vertices(G)
    s.predecessor = None # s krijgt het attribuut 'predecessor'
    s.distance = 0 # s krijgt het attribuut 'distance'
    for v in V:
        if v != s:
            v.distance = INFINITY # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s) # plaats de startnode in de queue
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u # v krijgt het attribuut 'predecessor'
                q.enqueue(v)      # plaats v in de queue
    for v in V:
        if v.distance == INFINITY:
            return False
    return True

def is_strongly_connected(G, start):
    if is_connected(G, start):
        V = vertices(G)
        nG = {}
        for u in V:
            nG[u] = []
        for u in V:
            for v in G[u]:
               nG[v].append(u)
        print("test:",nG)
        return is_connected(nG, start)
    return False


v = [Vertex(i) for i in range(3)]

G = {v[0]:[v[1]],
    v[1]:[v[2]],
    v[2]:[v[0]]}

print(is_strongly_connected(G,v[0]))

v = [Vertex(i) for i in range(3)]

G = {v[0]:[v[1]],
    v[1]:[],
    v[2]:[v[0], v[1]]}
    
print(is_strongly_connected(G,v[0]))