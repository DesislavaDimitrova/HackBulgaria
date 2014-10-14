#Counting all consonants in a given string

def count_consonants(str):
	str = str.lower()
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
	count = 0
	for i in str:
		if i in consonants:
			count += 1
	return count

