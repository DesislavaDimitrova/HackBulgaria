#Checking if needle is part of the fibonacci sequence, created by listA and listB for the first two elements
def member_of_nth_fib_lists(listA, listB, needle):
    i = 2
    while i < 10: 
        next_list = listA + listB
        listA = listB
        listB = next_list
        i += 1
    return ''.join(map(str, needle)) in ''.join(map(str, listA))
