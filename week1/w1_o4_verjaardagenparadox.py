import random

tempLijst = []
lijst = []
for i in range(1, 101):
    for j in range(1, 24):
        tempLijst.append(random.randint(1, 366))
    lijst.append(tempLijst)
    tempLijst = []

"""
description
count matching items in a two dimensional list

parameter
------
lijst : list
    this has to be a two dimensional list
    
return
------
matches : int
    the amount of matches found

"""
def countMatchesInNestedList(lijst):
    assert (type(lijst[0])) == list, "not a two dimensional list" 

    matches = 0

    for i in lijst:
        start = 1
        for j in i:
            for k in range(start, len(i)):
                if(j == i[k]):
                    matches += 1
                    break
            start += 1
    return matches

print("Amount of lists with matching numbers:", countMatchesInNestedList(lijst))
