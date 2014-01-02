def chain_end(n):
	if n == 89:
		return True
	if n == 1:
		return False
	next = 0
	while n > 0:
		next += (n % 10)**2
		n = n / 10
	return chain_end(next)

count = 0
for x in xrange(1,10000000):
	if chain_end(x):
		count += 1

print count
