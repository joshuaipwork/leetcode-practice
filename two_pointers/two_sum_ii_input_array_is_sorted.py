from typing import Union

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> Union(list[int], None):
        """
        Memory: O(1)
        Runtime: O(n)

        Searches through an array of integers for a pair of integers that
        add up to the target.

        Args:
            numbers (list of int): The array to search. It must be sorted
                such that the list is in non-decreasing order.
            target (int): The sum to search for in the array.
        Returns:
            (list of int or None): A list containing the solution, 1-indexed.
                If no solution is available, returns None.
        """
        # init values
        left: int = 0
        right: int = len(numbers) - 1

        # while we haven't found the solution
        while left < right:
            # add values and compare to target
            num_sum: int = numbers[left] + numbers[right]
            
            # check if we found it, if so break and return result
            if num_sum == target:
                return [left + 1, right + 1]
            # if sum is less move left index to the right
            elif num_sum < target:
                left += 1
            # if the sum is greater move right index to the left
            else:
                right -= 1
        return None
