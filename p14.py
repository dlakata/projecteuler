def collatz(n):
	count = 1
	if n == 0:
		return 0
	if n == 1:
		return count
	if n % 2 == 0:
		return count + collatz(n/2)
	if n % 2 != 0:
		return count + collatz(3*n + 1)

max_length = 0
max_start = 0

for x in xrange(1000000):
	length = collatz(x)
	if length > max_length:
		max_length = length
		max_start = x

print max_start
