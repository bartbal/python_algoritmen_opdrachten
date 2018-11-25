"""
description
this function extracts all numbers from a string. the numbers get grouped if they are separated with a char

parameter
------
a : string
    this is the string where the function searches in

return
------
numbers : list
    this function returns a list with the numbers it found

"""
def getNumbers(a):
    assert (type(a) == str), "a is not a string"
    numbers = []
    temp = ''
    for i in range(0, len(a)):
        if(a[i] > '0' and a[i] < '9'):
            temp += a[i]
            if(len(a)-1 == i):
                numbers.append(int(temp))
        elif(temp != ''):
            numbers.append(int(temp))
            temp = ''
    return numbers

print(getNumbers("halli123hoegaat1315het12"))
# print(getNumbers([1, 4, 6]))