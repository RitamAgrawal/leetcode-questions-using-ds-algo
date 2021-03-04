# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def binaryToDecimal(binary): 
            binary1 = binary 
            decimal, i, n = 0, 0, 0
            while(binary != 0): 
                dec = binary % 10
                decimal = decimal + dec * pow(2, i) 
                binary = binary//10
                i += 1
            return decimal

        def path(root,add):
            if root== None:
                return 0
            else:
                add = add * 10 + root.val
                print add
            if root.left == None and root.right == None:
                return binaryToDecimal(add)
            return path(root.left, add) + path(root.right,add)
        return path(root,0)
        