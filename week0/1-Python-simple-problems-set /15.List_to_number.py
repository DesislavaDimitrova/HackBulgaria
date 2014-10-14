#Turning a list of digits into a number

def list_to_number(digits):
	number = ''.join(map(str, digits))
	return int(number)

