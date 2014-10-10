#Finding if an integer is a palindrome

def is_int_palindrome(n):
	n_str = str(n)
	for i in range(int(len(n_str) / 2)):
		if n_str[i] == n_str[len(n_str)- i - 1]:
			return True
	return False
