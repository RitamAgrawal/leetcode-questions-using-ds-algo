# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        result = []
        while (head!= None):
            result.append(head.val)
            head = head.next
        output= 0        
        x = 0    
        while result:
            output = (result.pop() * (2**x))+output
            x += 1        
        return output