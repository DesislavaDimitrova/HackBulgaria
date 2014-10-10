#Checking if integer is prime

def is_prime(n):
    import math   
    if n < 2: 
        return False
    elif n == 2: 
        return True
    else:
        for div in range(2, int(math.sqrt(n)) + 1):  
            if n % div == 0:
                return False    
        return True

def main():
    print(is_prime(8)) 

if __name__ == '__main__':
    main()


