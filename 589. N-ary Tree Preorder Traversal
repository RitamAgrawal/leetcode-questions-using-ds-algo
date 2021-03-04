class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def traversal(root):
            if root is None: return
            result.append(root.val)
            for i in root.children:
                traversal(i)
        
        traversal(root)
        return result