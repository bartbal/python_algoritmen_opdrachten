"""
description
find the highest number in a list. this list must consist of either integers or floats. the list must have at least a length of 1

parameter
------
a : list
    this is the list to search in for the highest number

return
------
max : int, float
    this function returns the highest int or float that it found

"""
def mymax(a):
    max = 0;
    assert(len(a) != 0), "list of 0"
    for i in a:
        assert(type(i) == float or type(i) == int), "type not float"
        if(i > max):
            max = i
    return max

print(mymax([7.0,3.4,8.6,3.2,5.5,1.8,5.9,3.3,6.9,6.0,9.1,9.5,3.0,10.2,33.6,66.7,24.1]))
print(mymax([7,3,8,3,5,1,5,3,6,6,9,9,3,10,33,66,24]))
# print(mymax([]))
# print(mymax(['i', 'h']))