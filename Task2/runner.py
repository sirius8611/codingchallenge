import heapq
class Node:
    def __init__(self, x, y, p, parent):
        self.x = x
        self.y = y
        self.p = p
        self.parent = parent

    def __lt__(self, other):
        return self.p < other.p

class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple(int, Node)] = []
    def empty(self) -> bool:
        return len(self.elements) == 0
    def push(self, p, item):
        heapq.heappush(self.elements, (p, item))
    def pop(self):
        return heapq.heappop(self.elements)[1]