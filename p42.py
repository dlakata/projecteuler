import math

f = open('words.txt', 'r')
string = f.read().replace("\"", "")
words = sorted(string.split(","))

def letter_score(word):
	score = 0
	for x in xrange(len(word)):
		c = word[x:1+x]
		score += ord(c) - 64
	return score

def is_triangular(n):
	sqrt = int(math.sqrt(8 * n + 1))
	return sqrt * sqrt == 8 * n + 1

count = 0
for word in words:
	if is_triangular(letter_score(word)):
		count += 1

print count