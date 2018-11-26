"""
description
Recursive function for marking non prime numbers.

parameter
------
numbers : list
    This is a list filled with True booleans. The indexes are used as the numbers. Non prime indexes get set as False

prime : int
    This is the prime number the function is at now. This has a default value and is used for the recursion.
    it does not have to be set on initial call.

return
------
:list
    This function returns a list with booleans. If the index of the boolean is not a prime number it is marked as False

"""
def marker(numbers, prime = 2):
    target = prime * prime

    for i in range(0, len(numbers)):
        if(i >= target):
            if(i == target):
                numbers[i] = False
            target += prime

    for i in range(prime+1, len(numbers)):
        if(numbers[i] == True):
            prime = i
            break
        if(i+1 == len(numbers)):
            return numbers

    return marker(numbers, prime)


"""
description
This function applies the Sieve of Eratosthenes method to locate the prime numbers in a range of 1 to length

parameter
------
length : int
    This defines the max number of a range from 1
    
return
------
prime : list
    This the list with prime numbers it found

"""
def zeefVanEratosthenes(length):
    numbers = [True] * length
    numbers = marker(numbers)

    prime = []
    for i in range(1, len(numbers)):
        if(numbers[i]):
            prime.append(i)

    return prime

result = zeefVanEratosthenes(1000)

# check if result is correct
print("Correct result:", result == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])

# print result
print("Result:", result)
