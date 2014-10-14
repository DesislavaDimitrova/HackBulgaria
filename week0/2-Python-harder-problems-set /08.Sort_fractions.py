#Returning the fraction in it's irreducible form
def simplify_fraction(fraction):
	div = 2
	while div <= fraction[0]:
		while fraction[0] % div == 0 and fraction[1] % div == 0:
			fraction = (int(fraction[0] / div), int(fraction[1] / div))
		div += 1
	return fraction

#Returning a list of tuples(nominator, denominator), sorted in increasing order
def sort_fractions(fractions):
	for index, item in enumerate(fractions):
		fractions[index] = simplify_fraction(item)
	return sorted(fractions, key = lambda x: (x[0]/x[1]))

