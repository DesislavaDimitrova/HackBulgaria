#Counting all consonants in a given string

def count_consonants(str):
	str = str.lower()
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
	count = 0
	for str_item in str:
		for index, consonants_item in enumerate(consonants):
			if str_item == consonants_item:
				count += 1
	return count

def main():
	print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")) 

if __name__ == '__main__':
	main()