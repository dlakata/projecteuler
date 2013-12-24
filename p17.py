def ones(n):
	if n == 0:
		return 0

def tens(n):
	return n


def count(n):
	length = len(str(n))
	if length == 1:
		return ones(n)
	if length == 2:
		one = n % 10
		ten = int(str(n)[:1])
		return tens(ten) + ones(one)
	if length == 3:
		one = n % 10
		ten = int(str(n)[1:2])
		hun = int(str(n)[:1])
		return 7 + tens(ten) + ones(one)
	if length == 4:
		return 11

print len(str(400))
	
