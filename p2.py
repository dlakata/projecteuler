fib1 = 1
fib2 = 2
temp = 0
sum = 0
while(fib2 < 4000000):
	temp = fib2
	fib2 = fib1 + fib2
	fib1 = temp
	if fib1 % 2 == 0:
		sum += fib1

print(sum)