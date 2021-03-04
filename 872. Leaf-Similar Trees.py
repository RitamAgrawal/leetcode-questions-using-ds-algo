class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        traversal1 = []
        traversal2 = []
        
        def searchleaf(root, traversal): 
            if root== None: return
            if root.left == None and root.right == None:
                traversal.append(root.val)
            else:
                searchleaf(root.left, traversal)
                searchleaf(root.right, traversal)
            return traversal

        sequence1 = searchleaf(root1, traversal1)
        sequence2 = searchleaf(root2, traversal2)
        
        size1 = len(sequence1)
        size2 = len(sequence2)
        if sequence1 == sequence2:
            return True
        else:
            return False
        
            
           
        
        