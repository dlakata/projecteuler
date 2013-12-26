def ones(n):
	if n == 0:
		return 0
	if n == 1 or n == 2 or n == 6 or n == 10:
		return 3
	if n == 4 or n == 5 or n == 9:
		return 4
	if n == 3 or n == 7 or n == 8:
		return 5

def two_digit(n):
	if n == 11 or n == 12 or n == 20:
		return 6
	if n == 13 or n == 14 or n == 18 or n == 19:
		return 8
	if n == 15 or n == 16:
		return 7
	if n == 17:
		return 9
	# for two-digit numbers greater than 20...
	if n == 2 or n == 3 or n == 8 or n == 9:
		return 6
	if n == 4 or n == 5 or n == 6:
		return 5
	if n == 7:
		return 7


def count(n):
	length = len(str(n))
	if n <= 10:
		return ones(n)
	if length == 2:
		if n <= 20:
			return two_digit(n)
		one = n % 10
		ten = int(str(n)[:1])
		return two_digit(ten) + ones(one)
	if length == 3:
		tens = n % 100
		hun = int(str(n)[:1])
		if tens == 0:
			return ones(hun) + 7
		return ones(hun) + 10 + count(tens)
	if length == 4:
		return 11

sum = 0
for x in range(1,1001):
	sum += count(x)

print sum
	
