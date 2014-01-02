import math

def is_prime(n):
	if n == 1 or n == 0:
		return False
	for x in range(2,int(math.sqrt(n)+1)):
		if n % x == 0:
			return False
	return True

def prime_left_right(n):
	num = str(n)
	i = 1
	check = ""
	while i < len(num) + 1:
		check = num[-i:]
		if not(is_prime(int(check))):
			return False
		i += 1
	return True

def prime_right_left(n):
	while n > 0:
		if not(is_prime(n)):
			return False
		n = n / 10
	return True

def sum_truncatable_primes():
	count = 0
	sum = 0
	for x in xrange(10,10000000):
		if count == 11:
			break
		if is_prime(x) and prime_right_left(x) and prime_left_right(x):
			sum += x
			count += 1
	return sum

print sum_truncatable_primes()
