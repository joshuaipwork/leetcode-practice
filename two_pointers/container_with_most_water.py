class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Memory: O(1)
        Runtime: O(n)

        Args:
            height (list of int): a list representing the heights of possible sides
        Returns:
            (int): The best area that can be formed by selecting two heights from
                the height array and finding the area formed by min(height[i], height[j]) *
                j - i, where j > i. 
        """
        # init variables
        left_index: int = 0
        right_index: int = len(height) - 1
        best_volume: int = 0

        while left_index < right_index:
            # calculate the current volume
            volume = (right_index - left_index) * min(height[left_index], height[right_index])
            # compare it to the best
            best_volume = max(volume, best_volume)

            # whichever value is smaller shift it
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        
        return best_volume