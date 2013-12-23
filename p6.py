individualSum = 0
totalSum = 0

for x in range(1,101):
	individualSum += x * x
	totalSum += x

print(totalSum * totalSum - individualSum)