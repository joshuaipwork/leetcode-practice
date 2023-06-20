# The lesson here is to always read the problem.
# When filling this out for the first time, I misread the problem
# and didn't realize that non-alphanumeric characters should be ignored.
# I also didn't realize that case wasn't important. 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Memory: O(1)
        Runtime: O(n)

        Checks if a string is a valid palindrome. A string is a valid
        palindrome if the string is identical when reversed, 
        ignoring non-alphanumerical characters and cases.

        Args:
            s (str): The string to check.
        Returns:
            True if the string s is a valid palindrome, False otherwise.
        """
        left_index: int = 0
        right_index: int = len(s) - 1

        while left_index < right_index:
            if not s[left_index].isalnum():
                left_index += 1
                continue
            if not s[right_index].isalnum():
                right_index -= 1
                continue
            if s[left_index].upper() != s[right_index].upper():
                return False
            left_index += 1
            right_index -= 1

        return True