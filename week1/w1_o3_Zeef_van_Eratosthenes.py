"""
description
recursive function for marking non prime numbers.

parameter
------
pointer : int
    this is the number used to find which numbers have to be marked

numbers : list
    this is a list of numbers to search in.

marked : list
    this is a list with the marked numbers. this has a default value and is used for the recursion.
    it does not have to be set on initial call

return
------
:list
    this function returns a list with the numbers it marked

"""
def marker(pointer, numbers, marked = []):
    if(pointer > max(numbers)):
        return marked

    target = pointer*pointer

    for i in numbers:
        if(i >= target):
            if(i == target):
                marked.append(i)
            target += pointer

    while(True):  # this is to increment the pointer the correct amount of times
        pointer += 1
        if(pointer not in marked):
            print(pointer, marked)
            break

    return marker(pointer, numbers, marked)


"""
description
this function applies the Sieve of Eratosthenes method to locate the prime numbers in a list of numbers

parameter
------
numbers : list
    this is a list of numbers to search in.
    
return
------
:list
    this the list with prime numbers it found

"""
def zeefVanEratosthenes(numbers):
    pointer = 2
    marked = marker(pointer, numbers)
    return ([x for x in numbers if x not in marked], [x for x in marked if x not in numbers])[0]

# create a list of the numbers 1 to 1000
numbers = []
for i in range(1, 1001):
    numbers.append(i)

# call the zeefVanEratosthenes function
# print(zeefVanEratosthenes(numbers))
print(zeefVanEratosthenes(numbers) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])
