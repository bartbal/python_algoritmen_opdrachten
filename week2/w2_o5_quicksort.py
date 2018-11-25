import random

"""
description
swap 2 list items with each other

parameter
------
a : list
    this is the list where to swap in
i : int
    this is the index of one item to swap
j : int
    this is the index of the other item to swap

"""
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


count = 0

"""
description
this recursive function sorts a list using a Quicksort algorithm 

parameter
------
a : list
    this is the list where to swap in
low : int
    this the start index of the list
high : int
    this is the end index of the list

"""
def qsort(a, low=0, high=-1):
    global count
    count += 1
    if high == -1:
        high = len(a) - 1
    count += 1
    if low < high:
        swap(a, low, low)
        # swap(a, low,  random.randint(low, high))
        m = low
        for j in range(low+1, high+1):
            count += 1
            if a[j] < a[low]:
                m += 1
                swap(a, m, j)
                            # low < i <= m : a[i] < a[low]
                            # i > m : a[i] >= a[low]
                swap(a, low, m)
                            # low <= i < m : a[i] < a[m]
                            # i > m : a[i] >= a[m]
        count += 1
        if m > 0:
            qsort(a, low, m-1)
        qsort(a, m+1, high)


lijst = []
for i in range(0, 10000):
    lijst.append(random.randint(0, 1000))

qsort(lijst, 0, 9999)
print(count)

# normaal resultaat van count = 1508991
# resultaat met pivot op laag = 1540801