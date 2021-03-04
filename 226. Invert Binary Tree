class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop()
                # left = cur.left
                # right = cur.right
                # cur.left = right
                # cur.right = left
                cur.right, cur.left = cur.left, cur.right

                if cur.right:
                    queue.append(cur.right)

                if cur.left:
                    queue.append(cur.left)
        return root