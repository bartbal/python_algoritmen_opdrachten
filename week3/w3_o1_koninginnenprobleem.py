def check(a,i):
    # ga na of i aan a toegevoegd kan worden   
    n = len(a)   
    return not (i in a or i+n in [a[j]+j for j in range(n)] or i-n in [a[j]-j for j in range(n)]) 

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:  
                print("X",end= " ")
            else:
                print("*",end= " ")
        print()
    print()
def rsearch(N):
    global count
    global a
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a) == N:
                count += 1
                print(a)
                rsearch(N)
                # return True# geschikte a gevonden
            else: 
                if rsearch(N):
                    return True
            del a[-1] # verwijder laatste element   
    return False

a = [] # a geeft voor iedere rij de kolompositie 
count = 0
aant = 0
rsearch(8)
printQueens(a)
print(count)