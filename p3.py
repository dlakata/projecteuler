import math

def is_prime(n):
	if n == 1:
		return False
	for x in range(2,int(math.sqrt(n)+1)):
		if n % x == 0:
			return False
	return True

def greatest_prime_factor(n):
	max = 0
	left = n
	while left != 1:
		i = 2
		while left % i != 0:
			i = i + 1
		left = left / i
		if i > max:
			max = i
	return max

print greatest_prime_factor(600851475143)