#Counting occurrences of words in dictionary

def count_words(arr):
	d = {}
	for index, item in enumerate(arr):
		count = arr.count(item)
		d[item] = count
	return d

