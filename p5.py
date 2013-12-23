def greatest_number():
	n = 20
	while(True):
		for x in range(11,21):
			if n % x != 0:
				break
			if x == 20:
				return n
		n += 20

print greatest_number()