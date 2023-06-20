# 

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Memory: O(1)
        Runtime: O(log n)
        Args:
            nums (list of int): An array of integers sorted
                in ascending order.
            target (int): the integer to find the index of
        Returns:
            (int): the index of the integer in nums. If the
                integer does not exist, return -1
        """
        if not nums:
            return -1
        if nums[len(nums) - 1] == target:
            return len(nums) - 1
        if nums[0] == target:
            return 0
        
        left_index = 0
        right_index = len(nums) - 1

        while left_index < right_index:
            # select the midway point
            next_index = (left_index + right_index) // 2

            # 
            if nums[next_index] == target:
                return next_index
            # 
            elif nums[next_index] > target:
                right_index = next_index - 1
            # 
            else:
                # This + 1 tripped me up earlier.
                left_index = next_index + 1

        return -1

