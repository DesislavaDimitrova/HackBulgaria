#Counting occurrences of words in dictionary
def count_words(arr):
	d = {}
	for index, item in enumerate(arr):
		count = arr.count(item)
		d[item] = count
	return d

#Returning the number of different words in a arr
def unique_words_count(arr):
	d2 = count_words(arr)
	count = len(d2)
	return count
