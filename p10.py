import math

def is_prime(n):
	if n == 1:
		return False
	for x in range(2,int(math.sqrt(n)+1)):
		if n % x == 0:
			return False
	return True
sum = 0
for x in range(0,2000000):
	if is_prime(x):
		sum = sum + x

print sum