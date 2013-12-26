import math

# Triangular numbers defined by T(n) = n * (n + 1) / 2
# (as provided by Problem 42)
# Original function:
# def triangle_number(n):
#	num = 0
#	while n > 0:
#		num += n
#		n -= 1
#	return num
def triangle_number(n):
	return n * (n + 1) / 2

def num_of_divisors(n):
	num = 1
	check = int(math.sqrt(n))
	while check > 1:
		if n % check == 0:
			num += 1
		check -= 1
	return 2 * num

i = 1
while(True):
	if num_of_divisors(triangle_number(i)) > 500:
		print triangle_number(i)
		break
	i += 1
