# When reversing a linked list or doing other things with the head, you
# need to set the head to point to nothing, otherwise you'll have a loop.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Memory: O(1)
        Runtime: O(n) 

        Iterative solution
        """
        if not head or not head.next:
            return head
        
        current = head
        next = head.next
        current.next = None

        while next:
            new_next = next.next
            next.next = current
            current = next
            next = new_next
        
        return current

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Memory: O(n)
        Runtime: O(n)

        Recursive Solution
        """
        return self.reverseNode(None, head)

    def reverseNode(self, last: Optional[ListNode], current: ListNode) -> Optional[ListNode]:
        """
        Helper function for reverseList. Reverses a single node, then recursively reverses
        the next node.
        """
        if not current:
            return last
        
        new_next = current.next
        current.next = last

        return self.reverseNode(current, new_next)