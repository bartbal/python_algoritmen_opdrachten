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

    while n > 0:

        if n % 2 == 0:

            machten = machten * machten
            n//= 2

        else:
            m = m * machten
            n -= 1

        count += 1


    return m

print("answer: ", machtv3(2,10000))
print("amound of multiplications:", count)
