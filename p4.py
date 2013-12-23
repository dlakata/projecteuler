def is_palindrome(n):
	n_str = str(n)
	length = n_str.__len__()
	for x in range(0,int(length/2)):
		if n_str[x] != n_str[length - x - 1]:
			return False
	return True

list = []

for x in range(0,999):
	for y in range(0,999):
		if is_palindrome(x*y):
			list.append(x*y)

max = 0
for x in list:
	if x > max and is_palindrome(x):
		max = x


print max