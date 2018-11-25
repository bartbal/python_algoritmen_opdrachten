count = 0
"""
description
this function calculates a to the power of n

parameter
------
a : int
    number you want to perform the calculation on
    
n : int
    this number is the power

return
------
m : int or float
    this is the result of the calculation given as an int or a float

"""
def machtv3(a,n):
    global count
    assert n > 0

    m = 1
    machten = a

    bexpand = "{0:b}".format(n)

    for c in reversed(bexpand):

        if c == '1':
            count += 1
            m = m * machten

        count += 1
        machten = machten * machten


    return m

print("answer", machtv3(2,10000))
print("amound of multiplications:", count)
