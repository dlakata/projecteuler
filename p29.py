import math

set = set()

for a in range(2,101):
	for b in range(2,101):
		set.add(math.pow(a,b))

print len(set)
