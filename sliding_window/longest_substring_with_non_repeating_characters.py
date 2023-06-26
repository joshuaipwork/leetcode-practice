class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        """
        Runtime: O(n)
        Memory: O(n)

        Determines the length of the longest substring which can be
        created from the input string without repeating characters within
        the substring.

        Args:
            string (str): The string to analyze
        Returns:
            (int): The length of the longest substring in the input string
                without repeating characters.
        """
        # create data structures
        characters: set[str] = set()
        left: int = 0
        right: int = 0
        max_length: int = 0
        while right < len(string):
            if string[right] not in characters:
                characters.add(string[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                characters.remove(string[left])
                left += 1
        return max_length