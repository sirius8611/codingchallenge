dirs = [[0, -1], [-1, 0], [0,1], [1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]
def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))
def color(n, m, grid):
    coloring = [False, False, False, False]
    color_grid = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if x % 2 == 0 and y % 2 == 0 and grid[x][y] != 1:
                coloring[0] = True
                color_grid[x][y] = 1
            elif x % 2 == 0 and y % 2 != 0 and grid[x][y] != 1:
                coloring[1] = True
                color_grid[x][y] = 2
            elif x % 2 != 0 and y % 2 == 0 and grid[x][y] != 1:
                coloring[2] = True
                color_grid[x][y] = 3
            elif x % 2 != 0 and y % 2 != 0 and grid[x][y] != 1:
                coloring[3] = True
                color_grid[x][y] = 4
    colors = coloring.count(True)
    print(colors)
    print_grid(color_grid)
def main():
    inFile = './sample1.inp'
    f = open(inFile, 'r')
    line = f.readline()
    n, m, k = [int(x) for x in line.split()]
    grid = [[0] * m for _ in range(n)]
    for ii in range(k):
        line = f.readline()
        xx, yy = [int(x) for x in line.split()]
        grid[xx][yy] = 1
    color(n, m, grid)

main()

