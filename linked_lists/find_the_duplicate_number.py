class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Memory: O(1)
        Runtime: O(n)

        This function implements Floyd's tortoise and hare algorithm for finding the start of a cycles in a list.
        1. Create two pointers, called tortoise and hare. Tortoise starts out at position 1, Hare starts at position 2
            - You can use a do-while loop or a while loop that iterates tortoise and hare before checking equality
        2. Tortoise moves once at each iteration. Hare moves twice at each iteration. Iterate until tortoise == hare
        3. Create a third pointer. This pointer, follower, also moves once per iteration
        4. Iterate tortoise and follower until they are equal. When they are equal, that is the start of the cycle.
        """
        tortoise: int = 0
        hare: int = 0

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        follower = 0
        while True:
            follower = nums[follower]
            tortoise = nums[tortoise]
            if follower == tortoise:
                return tortoise