#Checking if a number is balanced

def is_number_balanced(n):
	n_str = str(n)
	left_sum = 0
	right_sum = 0
	first_part = n_str[:len(n_str)//2]
	for i, item in enumerate(first_part):
		left_sum += int(item)
	if len(n_str) % 2 == 0:
		second_part = n_str[len(n_str)//2:]
	else: 
		second_part = n_str[len(n_str)//2 + 1:]
	for i, item in enumerate(second_part):
		right_sum += int(item)
	return left_sum == right_sum


