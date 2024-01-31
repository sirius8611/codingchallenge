import os
import pandas
import numpy as np

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
    listInp = []
    for dirname, _, filenames in os.walk('./sample/'):
        for filename in filenames:
            if filename[-3:]  == 'inp':
                listInp.append(os.path.join(dirname, filename))
    listInp = sorted(listInp)

    for idx, filename in enumerate(listInp):
        '''
        this is read file template
        '''
        input_file = filename
        counter = filename.split('.')[1].split('/')[-1]
        counter = int(counter[6:])


        inFile = filename
        if not os.path.exists('./result'):
            os.mkdir('./result')
        
        outFile = f'./result/sample{counter}.out'

        f = open(inFile, 'r')
        line = f.readline()
        n, m, k = [int(x) for x in line.split()]
        listBlocks = []
        grid = [[0] * m for _ in range(n)]
        for ii in range(k):
            line = f.readline()
            xx, yy = [int(x) for x in line.split()]
            grid[xx][yy] = 1

        lline = f.readline()
        sx, sy, ex, ey = [int(x) for x in lline.split()]
        grid[sx][sy] = 2
        grid[ex][ey] = 2
        color(n, m, grid)

main()
