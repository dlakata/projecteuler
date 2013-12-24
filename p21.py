def sum_of_divisors(n):
	sum = 0
	check = n / 2
	while check > 0:
		if n % check == 0:
			sum += check
		check -= 1
	return sum

amicables = set()

for x in xrange(10001):
	a = sum_of_divisors(x)
	b = sum_of_divisors(a)
	if b == x and a != b:
		amicables.add(a)
		amicables.add(b)

print sum(amicables)
