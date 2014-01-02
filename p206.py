def check(n):
	n_str = str(n)
	if n_str[0] != "1" or n_str[2] != "2" or n_str[4] != "3":
		return False
	if n_str[6] != "4" or n_str[8] != "5" or n_str[10] != "6":
		return False
	if n_str[12] != "7" or n_str[14] != "8" or n_str[16] != "9":
		return False
	if n_str[18] != "0":
		return False
	return True

def find():
	for x in xrange(1000000000,1400000000):
		if check(x**2):
			return x

print find()
