size = 3
grid = [[0 for i in range(size)] for j in range(size)]

def count_paths(i, j):
	if i == len(grid) - 1 and j == len(grid) - 1:
		return 1
	if i == len(grid) - 1:
		return count_paths(i,j+1)
	if j == len(grid) - 1:
		return count_paths(i+1,j)
	return count_paths(i,j+1) + count_paths(i+1,j)

print grid
