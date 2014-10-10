#Counting divisors of a number
def count_of_divisors(n):
    count = 0
    for div in range (1, n):
        if n % div == 0:
            count += 1
    return count + 1

#Checking if a number is prime
def is_prime(n):  
    import math  
    if n < 2: 
        return False
    elif n == 2: 
        return True
    else:
        for div in range(2, int(math.sqrt(n))+1):  
            if n % div == 0:
                return False    
        return True


#Checking if a number has a prime number of divisors
def prime_number_of_divisors(n):
    divisors = count_of_divisors(n)
    if is_prime(divisors):
        return True
    else:
        return False
