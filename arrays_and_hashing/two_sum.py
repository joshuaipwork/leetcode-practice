class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Memory: O(n)
        Runtime: O(n)

        Returns the indices of two numbers in nums which add
        up to target. Assumes that there must be exactly one
        such solution and the same element may not be reused.

        Args:
            nums (list of int): a list of numbers of any length
                containing exactly one pair of numbers which add up to
                target.
            target (int): the target value to be formed by
                the sum of two values in nums
        Returns:
            (list of int): a length 2 list containing the indices
                of the two values in nums which add up to the target. 
                order is not guaranteed.
        """
        complements: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in complements:
                return [i, complements[num]]
            else:
                complements[target - num] = i
