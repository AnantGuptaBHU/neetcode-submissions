"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        d = {}
        stack = []
        stack.append(node)
        while len(stack) != 0:
            a = stack.pop()
            if a not in d:
                newN = Node(a.val)
                d[a] = newN
            for neighbor in a.neighbors:
                if neighbor not in d:
                    stack.append(neighbor)
        for k,v in d.items():
            l = []
            for neighbor in k.neighbors:
                l.append(d[neighbor])
            v.neighbors = l
        return d[node]