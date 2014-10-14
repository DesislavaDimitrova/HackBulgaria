#Returning a list of tuples (pi, ai) - the result of the factorization of an integer
from collections import Counter

def prime_factorization(n):
	prime_divisors = [ ]
	i = 2
	while i*i <= n:
		while (n % i) == 0:
			prime_divisors.append(i)
			n /= i
		i += 1
	if n > 1:
		prime_divisors.append(n)
	d = Counter(prime_divisors)
	return list(d.items())


