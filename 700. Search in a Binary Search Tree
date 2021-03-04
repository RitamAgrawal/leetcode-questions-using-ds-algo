class Solution(object):
    def searchBST(self, root, value):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current_node = root
        if current_node == None:
            return None
        
        if value == current_node.val:
            return current_node
        
        if value < current_node.val:
            return self.searchBST(current_node.left, value)
            
        if value > current_node.val:
            return self.searchBST(current_node.right, value)