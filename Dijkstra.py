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
            
def Dijkstra(grid, start: Node, end: Node, n: int, m: int):
    visited = [[None for i in range(n)] for i in range(m)]
    visited[start.x][start.y] = start
    # visited[end.x][end.y] = end
    frontier = PriorityQueue()
    frontier.push(start.p, start)
    while not frontier.empty():
        current = frontier.pop()
        if current.x == end.x and current.y == end.y:
            return current
        for neighbor in nneighbors(current, grid):
            f = current.p + 1
            if (visited[neighbor[0]][neighbor[1]] == None):
                node = Node(neighbor[0], neighbor[1], f, current)
                visited[node.x][node.y] = node
                frontier.push(f, node)
            elif visited[neighbor[0]][neighbor[1]].p > f:
                visited[neighbor[0]][neighbor[1]].p = f
                visited[neighbor[0]][neighbor[1]].parent = current

def trace_path(node):
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