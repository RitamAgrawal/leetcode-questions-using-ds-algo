# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ##### Method 2
        carry = 0        
        l3_head_val = l1.val + l2.val        
        if l3_head_val >= 10:
            l3_head = ListNode(l3_head_val % 10)
            carry = l3_head_val // 10
        else:    
            l3_head = ListNode(l3_head_val)
        
        if l1.next == None and l2.next == None:
            if l3_head_val <= 9:
                l3_head = ListNode(l3_head_val)
            else:
                l3_head = ListNode(l3_head_val % 10)
                l3_head.next = ListNode(l3_head_val // 10)
            return l3_head
        l3 = l3_head        
        l1 = l1.next or ListNode(0)
        l2 = l2.next or ListNode(0)
        
        while l1.next or l2.next:
            current_frm_l1 = l1.val or 0
            current_frm_l2 = l2.val or 0
            sum_ = current_frm_l1 + current_frm_l2 + carry
            unit = sum_ % 10
            carry = sum_ // 10
            l3.next = ListNode(unit)
            l3 = l3.next
            l1 = l1.next or ListNode(0)
            l2 = l2.next or ListNode(0)
        l3_next_val = l1.val + l2.val + carry
        if l3_next_val >= 10:
            l3.next = ListNode(l3_next_val % 10)            
            l3.next.next = ListNode(l3_next_val // 10)            
        else:    
            l3.next = ListNode(l3_next_val)       
            
        return l3_head