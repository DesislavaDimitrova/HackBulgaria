#Counting iterations of NaN Expand

def iterations_of_nan_expand(expanded):
	not_a = "Not a "
	count = expanded.count("Not a ")
	if not count == (len(expanded) - 3) / 6 or not expanded[-3:] == "NaN":
		return False
	return expanded.count("Not a ") 


