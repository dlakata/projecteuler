f = open('names.txt', 'r')
string = f.read().replace("\"", "")
names = sorted(string.split(","))

def letter_score(name):
	score = 0
	for x in xrange(len(name)):
		c = name[x:1+x]
		score += ord(c) - 64
	return score

total = 0

for x in xrange(len(names)):
	total += (x + 1) * letter_score(names[x])

print total
