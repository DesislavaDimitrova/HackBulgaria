#Returning a dictionary, which keys are determined by the func argument

def groupby(func, seq):
	d = {}
	for i in seq:
		if func(i) in d:
			d[func(i)].append(i)
		else:
			d[func(i)] = [i]
	return d

