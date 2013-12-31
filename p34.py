import math

def check_digits(n):
	check = n
	sum = 0
	while check > 0:
		sum += math.factorial(check % 10)
		check = check / 10
	if sum == n:
		return True
	return False

sum = 0
for x in xrange(3,100001):
	if check_digits(x):
		sum += x

print sum