#Counting all vowels in a given string

def count_vowels(str):
	str = str.lower()
	vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	count = 0
	for str_item in str:
		for index, vowels_item in enumerate(vowels):
			if str_item == vowels_item:
				count += 1
	return count

