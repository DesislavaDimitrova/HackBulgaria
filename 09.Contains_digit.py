#Checking if a number contains a single digit

def contains_digit(number, digit):
	n_str = str(number)
	for i in n_str:
		if i == str(digit):
			return True
	return False