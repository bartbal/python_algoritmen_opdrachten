"""
description
make a string from the binary of an integer

parameter
------
n : int
    this is the integer to get the binary from

return
------
 : string
    this is the binary as a string

"""
def mybin(n):
    assert (n >= 0)

    if(n == 0):
        return ""

    return mybin(n >> 1) + str(n & 1)

print(mybin(35784))