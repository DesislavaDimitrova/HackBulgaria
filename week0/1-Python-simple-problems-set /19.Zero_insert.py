#Inserting 0 in-between if two neighboring digits are the same or their sum results in 0 when % 10

def zero_insert(n):
	n_lst = [int(x) for x in str(n)]
	for index, item in enumerate(n_lst):
		if n_lst[index - 1] == n_lst[index] or (n_lst[index-1] + n_lst[index]) % 10 ==0:
			n_lst.insert(index, 0)
	num = ''.join(map(str, n_lst))
	return int(num)

