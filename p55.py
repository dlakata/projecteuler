def is_palindrome(n):
	n_str = str(n)
	length = n_str.__len__()
	for x in range(0,int(length/2)):
		if n_str[x] != n_str[length - x - 1]:
			return False
	return True

def reverse(n):
	num = 0
	while n > 0:
		num *= 10
		num += n % 10
		n /= 10
	return num

def is_lychrel(n, count):
	rev = reverse(n)
	sum = rev + n
	if is_palindrome(sum):
		return False
	if count < 50:
		return is_lychrel(sum,count+1)
	else:
		return True

def count_lychrels():
	count = 0
	for x in xrange(1,10000):
		if is_lychrel(x,1):
			count += 1
	return count

print count_lychrels()
