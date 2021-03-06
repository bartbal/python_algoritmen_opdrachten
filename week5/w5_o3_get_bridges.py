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

def is_connected(G,s, target):
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
            if v == target:
                return True
            if v.distance == INFINITY: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u # v krijgt het attribuut 'predecessor'
                q.enqueue(v)      # plaats v in de queue
    return False

def get_bridges(G):
    bridges = []
    temp = None
    V = vertices(G)
    for u in V:
        for v in range(len(G[u])):
            temp = G[u][v]
            G[u].pop(v)
            G[temp].remove(u)
            if not is_connected(G, u, temp):
                bridges.append([u, temp])
            G[u].insert(v, temp)
            G[temp].append(u)
    return bridges

v = [Vertex(i) for i in range(8)]

G = {v[0]:[v[1],v[3]],
    v[1]:[v[0],v[2]],
    v[2]:[v[1],v[3],v[4]],
    v[3]:[v[0],v[2]],
    v[4]:[v[2],v[5],v[6]],
    v[5]:[v[4],v[6]],
    v[6]:[v[4],v[5], v[7]],
    v[7]:[v[6]]}

# print(is_connected(G,v[4], v[2]))
print("\nreslult:\n",get_bridges(G))