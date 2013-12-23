fib1 = 1
fib2 = 2
temp = 0
count = 2
limit = 1e2
while(fib2 < limit):
	temp = fib2
	fib2 = fib1 + fib2
	fib1 = temp
	count += 1

print fib2
