class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        def traversal(root):
            if root is None: return            
            for child in root.children:
                traversal(child)
            result.append(root.val)
        traversal(root)
        return result