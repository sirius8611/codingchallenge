from runner import PriorityQueue, Node

def potential(x: int, y: int, end: Node):
    return abs(x - end.x) + abs(y - end.y)

def nneighbors(node, grid):
    dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    result = []
    for dir in dirs:
        neighbour = [node.x + dir[0], node.y + dir[1]]
        if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[0]) and grid[neighbour[0]][neighbour[1]] != 1:
            result.append(neighbour)
    return result
            
def Astar(grid, start: Node, end: Node, j: int, coeff: int):
    visited = [[None for i in range(len(grid[0]))] for j in range(len(grid))]
    visited[start.x][start.y] = start
    # visited[end.x][end.y] = end
    frontier = PriorityQueue()
    frontier.push(start.p, start)
    while not frontier.empty():
        current = frontier.pop()
        if current.x == end.x and current.y == end.y:
            return current
        for neighbor in nneighbors(current, grid):
            if grid[neighbor[0]][neighbor[1]] == 0:
                f = coeff * (current.p + j) + potential(neighbor[0], neighbor[1], end)
            else:
                f = coeff * (current.p + grid[neighbor[0]][neighbor[1]])+ potential(neighbor[0], neighbor[1], end) 
            if (visited[neighbor[0]][neighbor[1]] == None):
                node = Node(neighbor[0], neighbor[1], f, current)
                visited[node.x][node.y] = node
                frontier.push(f, node)
            elif visited[neighbor[0]][neighbor[1]].p > f:
                visited[neighbor[0]][neighbor[1]].p = f
                visited[neighbor[0]][neighbor[1]].parent = current
    return None

def trace_path(node):
    if node == None:
        print("There's no path")
        return
    path = []
    cost = 1
    while node.parent != None:
        path.append([node.x, node.y])
        cost += 1
        node = node.parent
    path.append([node.x, node.y])
    path.reverse()
    print(cost)
    for i in range(len(path)):
        print('{0} {1}'.format(path[i][0], path[i][1]))


def main():
    inFile = 'sample/sample_task2.inp'
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

    start = Node(sx, sy, 0, None)
    end = Node(ex, ey, 0, None)


    next_line = f.readline()
    j, coeff = [int(x) for x in next_line.split()]
    trace_path(Astar(grid, start, end, j, coeff))

main()
