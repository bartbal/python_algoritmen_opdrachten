import random

ht = {}

while(True):
    x = random.uniform(0,1)
    h = hash(x) % (2**32)
    if h in ht:
        break
    ht[h] = x
    

print("match:")
print("x:",x, "y:",ht[h])
print("with hash:", h)

