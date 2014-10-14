#Checking if a number contains all digits

def contains_digits(number, digits):
	for index, item in enumerate(digits):
		if not (str(item) in str(number)):
			return False
	return True

