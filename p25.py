fib1 = 1
fib2 = 2
temp = 0
count = 3
while(len(str(fib2)) < 1000):
	temp = fib2
	fib2 = fib1 + fib2
	fib1 = temp
	count += 1

print count
