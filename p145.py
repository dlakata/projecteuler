def reverse(n):
	num = 0
	while n > 0:
		num *= 10
		num += n % 10
		n /= 10
	return num

def all_odd(n):
	while n > 0:
		if (n % 10) % 2 == 0:
			return False
		n /= 10
	return True

def is_reversible(n):
	if n % 10 == 0:
		return False
	sum = n + reverse(n)
	if all_odd(sum):
		return True
	return False

def count_reversibles():
	count = 0
	for x in xrange(1,1000000000):
		if x % 1000000 == 0:
			print x
		if is_reversible(x):
			count += 1
	return count

print count_reversibles()
