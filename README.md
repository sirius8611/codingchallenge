# Group 4 Documentation

### Problem 2

In this problem we use a star algorithm. 

**First we create a Node class.**

Node class has the following functions:

- Calculate_heuristic:
    - This function calculate the manhattan distance between two nodes in a grid
- equal
    - This function return a boolean stating whether two nodes are equal
- valid
    - This is a static method to check if the node is inside the grid and not a block
- __ lt __
    - This is a compare function which will later be used for priority queue

```jsx
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
```

**A star algorithm**

```python
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
```

First we create a priority queue that store the cost * efficient_value + steps + heuristic and the node then sort the queue to choose the smallest. From the chosen node, we move to the surround node and update the travel_cost of that node if the cost traveling from the current node is smaller than the current cost of that node. 

If the cost traveling from the current node is smaller than the current cost of that node, the trace array also store the parent node to that next node position. 

When print out the path, we just need to traverse backward from the end to its parent then looping until we reach the start node. 

### Problem 3

The solution is quite straightforward. Just coloring the surround of one node with 3 different colors. One way to do this is to color every two node with the same color. Group 4 color base on the even or odd of the location of the node that also ensure the color is colored every two node. 

```python
0 0 0 0 0                1 0 1 0 1                1 2 1 2 1
0 0 0 0 0       ->       0 0 0 0 0      ->        0 0 0 0 0
0 0 0 0 0                1 0 1 0 1                1 2 1 2 1
```

The maximum number of colors need to be used will be 4. If wanting to use less colors, the block will need to be on every two node of some dimensions.
