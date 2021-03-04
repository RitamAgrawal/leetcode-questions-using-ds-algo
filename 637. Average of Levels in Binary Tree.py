class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        output = []
        queue = []
        add = []
        queue.append(root)
        node = 1
        avg = root.val / node
        output.append(avg)
        num = 0
        while queue:
            size = len(queue)
            for i in range(size):
                current = queue.pop(0)

                if current.left:
                    queue.append(current.left)
                    num += 1
                    add.append(current.left.val)
                else:
                    l = 0
                if current.right:
                    queue.append(current.right)
                    num += 1
                    add.append(current.right.val)
                else:
                    r = 0
            if num > 0:                
                avg2 = sum(add) /num
                output.append(avg2)
                
            num = 0
            add.clear()
            
        return output