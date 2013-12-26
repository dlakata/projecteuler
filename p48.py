import math

def sum_series(n):
	sum = 0
	for a in range(1,n):
		sum += math.pow(a,a)
	return int(sum)

for x in range(1,201):
	print str(x) + ": " + str(sum_series(x))

