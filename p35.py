import math

def is_prime(n):
	if n == 1 or n == 0:
		return False
	for x in range(2,int(math.sqrt(n)+1)):
		if n % x == 0:
			return False
	return True

def check_circular_primes(n):
	num = str(n)
	length = len(num)
	i = 0
	while i < length:
		if not(is_prime(int(num))):
			return False
		num = num[1:] + num[0]
		i += 1
	return True

def count_circular_primes():
	count = 0
	for x in range(1000000):
		if check_circular_primes(x):
			count += 1
	return count

print count_circular_primes()
