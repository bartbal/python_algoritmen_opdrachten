import random

tempLijst = []
random_numbers = []
for i in range(1, 101):
    for j in range(1, 24):
        tempLijst.append(random.randint(1, 365))
    random_numbers.append(tempLijst)
    tempLijst = []

"""
description
count matching items in a two dimensional list

parameter
------
random_numbers : list
    this has to be a two dimensional list
    
return
------
matches : int
    the amount of matches found

"""
def countMatchesInNestedList(random_numbers):
    assert (type(random_numbers[0])) == list, "not a two dimensional list"

    matches = 0

    for numbers in random_numbers:
        start = 1
        for number in numbers:
            for k in range(start, len(numbers)):
                if(number == numbers[k]):
                    matches += 1
                    break
            start += 1
    return matches

print("Amount of lists with matching numbers:", countMatchesInNestedList(random_numbers))
