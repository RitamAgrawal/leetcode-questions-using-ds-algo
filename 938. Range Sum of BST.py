#Definition for a binary tree node.
#class TreeNode(object):
   #def __init__(self, val=0, left=None, right=None):
    #   self.val = val
     #  self.left = left
      # self.right = right

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        answer = 0
        stack = [root]
        while stack:
            Node = stack.pop()
            if Node:               
                if L <= Node.val <= R:
                    answer += Node.val
                if L < Node.val:
                    stack.append(Node.left)
                if Node.val < R:
                    stack.append(Node.right)
        return answer

    