"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
                return 0
        depth = 0
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            
            for i in range(size):
                current = queue.pop(0)
                for child in current.children:
                    queue.append(child)
            depth += 1
        return depth