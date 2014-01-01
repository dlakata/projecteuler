concat = "0"
count = 1

while len(concat) < 1000000:
	concat += str(count)
	count += 1

print int(concat[1]) * int(concat[10]) * int(concat[100]) * int(concat[1000]) * int(concat[10000]) * int(concat[100000])
