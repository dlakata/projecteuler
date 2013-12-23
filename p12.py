def triangle_number(n):
	num = 0
	while n > 0:
		num = num + n
		n = n - 1
	return num

def num_of_divisors(n):
	num = 2
	check = n / 2
	while check > 1:
		if n % check == 0:
			num = num + 1
		check = check - 1
	return num

i = 1
while(True):
	if num_of_divisors(triangle_number(i)) > 150:
		print triangle_number(i)
		break
	i = i + 1