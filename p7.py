import math

def is_prime(n):
	if n == 1:
		return False
	for x in range(2,int(math.sqrt(n)+1)):
		if n % x == 0:
			return False
	return True

def nth_prime(n):
	i = 2
	count = 0
	while(count != n):
		if is_prime(i):
			count += 1
		i += 1
	return i - 1

print(nth_prime(10001))