#Returning the n-th member of the fibonacci sequence

def nth_fib_lists(listA, listB, n):
    i = 2
    while i <= n:
        next_list = listA + listB
        listA = listB
        listB = next_list
        i += 1
    return listA


