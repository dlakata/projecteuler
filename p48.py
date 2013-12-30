def sum_series(n):
	sum = 0
	for a in range(1,n+1):
		sum += a**a
	return sum

print str(sum_series(1000))[-10:]
