#Checking if a number is balanced

def is_number_balanced(n):
	n_str = str(n)
	first_part = n_str[:len(n_str)//2]
	second_part = n_str[len(n_str)//2:]
	left_sum = 0
	right_sum = 0
	for i, item in enumerate(first_part):
		left_sum += int(item)
	for i, item in enumerate(second_part):
		right_sum += int(item)
	return left_sum == right_sum

def main():
	print(is_number_balanced(9)) 
	print(is_number_balanced(11)) 
	print(is_number_balanced(13)) 
	print(is_number_balanced(121))
	print(is_number_balanced(4518)) 
	print(is_number_balanced(28471)) 
	print(is_number_balanced(1238033))  

if __name__ == '__main__':
	main()