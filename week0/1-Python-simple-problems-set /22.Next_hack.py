#Finding if an integer is a palindrome
def is_int_palindrome(n):
	n_str = str(n)
	return n_str == n_str[::-1]


#Checking if an integer is a hack number - in binary is a palindrom and has an odd number of 1's
def is_hack_number(m):
	m_bin = bin(m)[2:]
	count = (str(m_bin)).count('1')
	if is_int_palindrome(m_bin) and not (count % 2 == 0):
		return True
	return False

#Returning next hack number, bigger than n """
def next_hack(n):
	n += 1
	while not is_hack_number(n):
		n+=1
	return n

