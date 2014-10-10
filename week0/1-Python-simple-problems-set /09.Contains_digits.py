#Checking if a number contains a single digit
def contains_digit(number, digit):
	n_str = str(number)
	for i in n_str:
		if i == str(digit):
			return True
	return False


#Checking if a number contains all digits
def contains_digits(number, digits):
	for i, item in enumerate(digits):
		if not (contains_digit(number, item)):
			return False
	return True
