#Checking if the given word is from the a^nb^n language

def is_an_bn(word):
	n = 1
	if word == '':
		return True
	while n <= 100:
		new_word = 'a' * n + 'b' * n
		n += 1
	if word in new_word:
		return True
	return False

