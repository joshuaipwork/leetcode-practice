# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # check for empty lists
        sum_head = ListNode(0, None) # a dummy node
        p1 = l1
        p2 = l2
        carried = 0
        ps = sum_head

        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            sum = val1 + val2 + carried
            carried = sum // 10
            digit = sum % 10
            ps.next = ListNode(digit, None)
            ps = ps.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        if carried:
            ps.next = ListNode(carried, None)
        
        return sum_head.next