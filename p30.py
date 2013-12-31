def check_digits(n):
	check = n
	sum = 0
	while check > 0:
		sum += (check % 10)**5
		check = check / 10
	if sum == n:
		return True
	return False

sum = 0
for x in xrange(2,1000000):
	if check_digits(x):
		sum += x

print sum