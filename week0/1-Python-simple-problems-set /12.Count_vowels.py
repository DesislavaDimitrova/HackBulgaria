#Counting all vowels in a given string

def count_vowels(str):
	str = str.lower()
	vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	count = 0
	for i in str:
		if i in vowels:
			count += 1
	return count

