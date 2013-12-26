size = 1001
spiral = [[0 for i in range(size)] for j in range(size)]

def populate_array(spiral):
	length = len(spiral)
	count = 1
	turn = 1
	center = length / 2
	current_i, current_j = center, center
	spiral[current_i][current_j] = count
	count += 1
	while current_i < length and current_i >= 0:
		if current_j >= length or current_j < 0:
			break
		for x in range(turn):
			current_i, current_j = next(4, current_i, current_j)
			if count == length * length + 1:
				break
			spiral[current_i][current_j] = count
			count += 1
		if count == length * length + 1:
			break
		for x in range(turn):
			current_i, current_j = next(2, current_i, current_j)
			spiral[current_i][current_j] = count
			count += 1
		turn += 1
		for x in range(turn):
			current_i, current_j = next(3, current_i, current_j)
			spiral[current_i][current_j] = count
			count += 1
		for x in range(turn):
			current_i, current_j = next(1, current_i, current_j)
			spiral[current_i][current_j] = count
			count += 1
		turn += 1

def next(direction, i, j):
	if direction == 1: # up
		return (i - 1, j)
	if direction == 2: # down
		return (i + 1, j)
	if direction == 3: # left
		return (i, j - 1)
	if direction == 4: # right
		return (i, j + 1)

def sum_diagonals(spiral):
	length = len(spiral)
	center = length / 2
	sum = spiral[center][center]
	for x in range(length):
		if x == center:
			continue
		sum += spiral[x][x]
	for x in range(length):
		if x == center:
			continue
		sum += spiral[x][length - 1 - x]
	return sum

populate_array(spiral)
print sum_diagonals(spiral)
