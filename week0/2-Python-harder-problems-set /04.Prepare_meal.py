def prepare_meal(number):
	num = number
	degree = 0
	while (num % 3) == 0:
		num //= 3
		degree += 1
	if number % 15 == 0:
		return 'spam ' * degree + 'and eggs'
	elif number % 3 == 0:
		return 'spam ' * degree
	elif number % 5 == 0:
		return 'eggs'
	else:
		return ''