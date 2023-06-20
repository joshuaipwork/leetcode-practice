class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Runtime: O(n)
        Memory: O(n)

        Args:
            nums (list of int): the list of numbers to check
        Returns:
            (bool): True if there is a duplicate in the list, False otherwise.
        """
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    def containsDuplicateInPlace(self, nums: list[int]) -> bool:
        """
        Runtime: O(n log n)
        Memory: O(1)

        Args:
            nums (list of int): the list of numbers to check
        Returns:
            (bool): True if there is a duplicate in the list, False otherwise.
        """
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
