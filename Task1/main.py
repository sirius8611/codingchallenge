import os
import pandas
import numpy as np
from runner import Node
from Dijkstra import trace_path, Dijkstra

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
    start = Node(sx, sy, 0, None)
    end = Node(ex, ey, 0, None)


    trace_path(Dijkstra(grid, start, end, n, m), outFile)