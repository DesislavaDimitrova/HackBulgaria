#Finding if an integer is a palindrome

def is_int_palindrome(n):
	n_str = str(n)
	return n_str == n_str[::-1]