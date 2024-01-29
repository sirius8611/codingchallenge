import os
import numpy as np

import heapq
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
    trace = {}
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
                trace[next_node.step] = cur_node
    
    if not found:
        print("There is no path")
    print(len(trace.keys()))
    for key in trace.keys():
        print(trace[key].x, end=" ")
        print(trace[key].y)
        


def main():
    inFile = './sample_task2.inp'

    outFile = 'sample/sample1.out'

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
    a_star_algorithm(start, end, grid,n, m, k)
main()