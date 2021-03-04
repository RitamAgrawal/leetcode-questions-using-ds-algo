class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root== None:
            return False
        if root:            
            queue = []
            r = root.val
            queue.append(root)
            while queue:
                size = len(queue)
                for i in range(size):
                    cur = queue.pop(0)
                    if cur.right:
                        if cur.right.val == r:
                            queue.append(cur.right)
                        else:
                            return False
                    if cur.left:
                        if cur.left.val == r:
                            queue.append(cur.left)
                        else:
                            return False
            return True
        return False