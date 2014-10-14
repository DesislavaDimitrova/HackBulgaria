#Summing of all numbers in a matrix

def sum_matrix(m):
	sum = 0
	for index, item in enumerate(m):
		for nested_index, nested_item in enumerate(item):
			sum += nested_item
	return sum
