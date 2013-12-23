import sys

a = 1
while (a < 500):
	b = 1
	while (b < 500):
		c = 1
		while (c < 500):
			if (a*a + b*b == c*c) and (a + b + c == 1000):
				print a*b*c
				sys.exit()
			c = c + 1
		b = b + 1
	a = a + 1