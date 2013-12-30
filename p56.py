def sum_digits(n):
	sum = 0
	while n > 0:
		sum += n % 10
		n = n / 10
	return sum

max = 0

for a in range(1,101):
	for b in range(1,101):
		sum = sum_digits(a**b)
		if sum > max:
			max = sum

print max
