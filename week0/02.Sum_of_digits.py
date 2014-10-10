#Summing all digits of a number

def sum_of_digits(n):
    if n < 0:
        n = abs(n)
    sum = 0
    while (n):
        sum += n % 10
        n //= 10

    return sum
