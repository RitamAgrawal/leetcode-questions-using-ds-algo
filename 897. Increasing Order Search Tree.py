# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Iterative approach
        if root == None: return
        stack = []
        head = None
        current = None
        temp = root
        
        while temp!= None:
            stack.append(temp)
            temp = temp.left
        
        while stack:
            temp2 = stack.pop()
            
            
            if head == None:
                head = temp2
                current = head
                
            else:
                current.left = None
                current.right = temp2
                current = current.right
                
            
            if temp2.right:
                
                stack.append(temp2.right)
                
                temp2 = temp2.right
                
                while temp2.left!=None:
                    
                    stack.append(temp2.left)
                    temp2 = temp2.left
                      
        return head
        # Recursive approach
        traversal = []
        def inorder(root, traversal):
            if root:
                inorder(root.left, traversal)
                traversal.append(root)
                inorder(root.right, traversal)
            return traversal
        
        stack = inorder(root,traversal)       
        
        new_root = stack.pop(0)        
        current = new_root
        while stack:
            current.left = None            
            current.right= stack.pop(0)               
            current = current.right
        return new_root
