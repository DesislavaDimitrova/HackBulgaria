#Returning the expansion of NaN that many times

def nan_expand(times):
	not_a = " "
	if times == 0:
		return not_a
	return "Not a " * times + "NaN"