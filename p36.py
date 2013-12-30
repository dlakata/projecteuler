import math

def is_palindrome(n):
	n_str = str(n)
	length = n_str.__len__()
	for x in range(0,int(length/2)):
		if n_str[x] != n_str[length - x - 1]:
			return False
	return True
	
def sum_palindromes():
	sum = 0
	for i in xrange(1,1000000):
		binary = int(bin(i)[2:])
		if is_palindrome(i) and is_palindrome(binary):
			sum += i
	return sum

print sum_palindromes()
