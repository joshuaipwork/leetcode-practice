# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # a dummy node makes the syntax a lot easier
        #   1. You can always check dummy.next, whether it's None
        #   2. The head is always dummy.next if it is a nonempty list
        #   3. You don't need to check if the tail exists or not since it is initialized to dummy
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next
            tail.next = next_node
            tail = tail.next

        # if only one list remains, just append the list
        # this prevents a lot of complicated logic in the while loop, and is also faster
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next