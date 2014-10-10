#Summing all divisors of an integer

def sum_of_divisors(n):
    sum = 0
    for divisors in range (1, n):
        if n % divisors == 0:
            sum += divisors
  
    return sum + n