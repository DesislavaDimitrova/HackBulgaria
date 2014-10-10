#Checking if there are n sevens in a row

def sevens_in_a_row(arr, n):
	count = 1
	for i in arr:
		if i == 7:
			count += 1
	if count == n:
		return True
	return False

def main():
	print(sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
if __name__ == '__main__':
	main()

