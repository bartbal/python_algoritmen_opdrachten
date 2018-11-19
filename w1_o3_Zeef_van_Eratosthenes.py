#priem = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

# create a global list from 1 to 1000
lijst = []
for i in range(1, 1001):
    lijst.append(i)

# define global list marked
marked = []

"""
description
recursive function for marking non prime numbers. it returns nothing but it changes some global variables

parameter
------
pointer : int
    this is the number used to find which numbers have to be marked

"""
def marker(pointer):
    global lijst
    global marked

    if(pointer > max(lijst)):
        return marked

    target = pointer*pointer

    for i in lijst:
        if(i >= target):
            if(i == target):
                marked.append(i)
            target += pointer
            if (i == target):
                marked.append(i)

    while(True):
        pointer += 1
        if(pointer not in marked):
            break

    marker(pointer)
    return


"""
description
this function applies the Sieve of Eratosthenes method to locate the prime numbers in a list of numbers

parameter
------
lijst : list
    this is a list of numbers to search in. this has to be a global variable
marked : list
    this is a list to store marked numbers in. this has to be a global variable

return
------
:list
    this function returns a list with prime numbers

"""
def zeefVanEratosthenes():
    global marked
    marked = []
    global lijst
    pointer = 2
    marker(pointer)
    return [x for x in lijst if x not in marked], [x for x in marked if x not in lijst]

print(zeefVanEratosthenes())