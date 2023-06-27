# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Memory: O(1)
        Runtime: O(n)
        """
        if head is None:
            return False
        
        # walker/runner is a classic model for cycle checking
        walker: ListNode = head
        runner: ListNode = head
        
        while True:
            # you can cgaub next.next to check two nodes ahead, and so on
            if runner.next is None or runner.next.next is None:
                return False
            if walker.next is None:
                return False
            
            walker = walker.next
            runner = runner.next.next

            if walker is runner:
                return True