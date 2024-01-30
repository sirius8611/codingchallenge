import os
import numpy as np
import sys
import heapq
import time
startTimer = float(time.time())
# grid
# start
# end
#Node classj
#Constants
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = 0
    @staticmethod
    #Calculate the manhattan distance between two nodes
    def calculate_heuristic(a, b, grid):
        return abs(a.x - b.x) + abs(a.y - b.y) + grid[a.x][b.y]
    @staticmethod
    def equal(a, b):
        return a.x == b.x and a.y == b.y
    @staticmethod
    def valid(a, n, m, grid):
        return a.x >= 0 and a.x < n and a.y >= 0 and a.y < m and grid[a.x][a.y] != 1
    
    def __lt__(self, other):
        return self.x < self.x
# class Distance:
#     def __init__(self, f, g):
#         self.f = f
#         self.g = g
    # @staticmethod
    # def a_star_algorithm(grid, start, end):
    #     return None
def a_star_algorithm(start, end, grid, n, m, eff):
    priority_queue = []
    distance_grid = [[999999] * m for _ in range(n)] 
    dirs = [[0, -1], [-1, 0], [0,1], [1, 0]]
    trace = [[Node(1,1)] * m for _ in range(n)]
    node_check = [[False] * m for _ in range(n)]
    distance_grid[start.x][start.y] = 0
    start.step = 0
    heapq.heappush(priority_queue, (0, start))
    found = False
    while priority_queue:
        cur_node = heapq.heappop(priority_queue)[1]
        step = cur_node.step
        node_check[cur_node.x][cur_node.y] = True
        if Node.equal(cur_node, end):
            found = True
            break
        for dir in dirs:
            next_node = Node(cur_node.x + dir[0], cur_node.y + dir[1])
            if not Node.valid(next_node, n, m, grid) or node_check[next_node.x][next_node.y]:
                continue
            g = step + 1 + eff * (distance_grid[cur_node.x][cur_node.y] + grid[next_node.x][next_node.y])
            if g < distance_grid[next_node.x][next_node.y]:
                distance_grid[next_node.x][next_node.y] = g
                h = Node.calculate_heuristic(next_node, end, grid)
                f = h + g
                next_node.step = step + 1
                heapq.heappush(priority_queue, (f, next_node))
                trace[next_node.x][next_node.y] = cur_node
    if not found:
        return None
    paths = []
    current = end
    while not Node.equal(current, start):
        paths.append(current)
        current = trace[current.x][current.y]
    paths.append(start)
    paths.reverse()
    return paths
    #trace function   
def print_path(paths):
    if not paths:
        print("0\n")
        return
    print(len(paths))
    for path in paths:
        print(path.x, end=" ")
        print(path.y)
        


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
        inFile = filename
        counter = filename.split('.')[1].split('/')[-1]
        counter = int(counter[6:])

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
        k = int(f.readline())
        for j in range(k):
            line = f.readline()
            x, y, w = [int(x) for x in line.split()]
            grid[x][y] = w
        llline = f.readline()
        j, k = [int(x) for x in llline.split()]
        for i in range(n):
            for y in range(m):
                if grid[i][y] == 0:
                    grid[i][y] = j  
        start = Node(sx, sy)
        end = Node(ex, ey)
        # print_grid(grid)
        if not os.path.exists('./result'):
            os.mkdir('./result')
    
        sys.stdout = open(f'./result/sample{counter}.out', 'w') 
        print_path(a_star_algorithm(start, end, grid,n, m, k))
main()
endTimer = float(time.time())
duration = (endTimer-startTimer) * 10**3
print("The time of execution of above program is :", duration, "ms")

sourceFile = open(f'./result/time.txt', 'w')
print(duration, file = sourceFile)
sourceFile.close()    

