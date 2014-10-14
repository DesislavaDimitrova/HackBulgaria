#Checking if integer is prime
import math

def is_prime(n):  
    if n < 2: 
        return False
    elif n == 2: 
        return True
    else:
        for div in range(2, int(math.sqrt(n)) + 1):  
            if n % div == 0:
                return False    
        return True


