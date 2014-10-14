#Checking if a given sequence is monotonously decreasing

def is_decreasing(seq):
	for i in range(1, len(seq)):
		if seq[i - 1] <= seq[i]:
			return False
	return True
