# In languages with mutable strings, it should be possible to sort
# each string, then compare them step by step for O(1) memory and
# O(n log n) runtime. However, python has immutable strings so this
# would just end up being O(n) memory O(n log n) runtime.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Memory: O(n)
        Runtime: O(n)

        Checks if t is an anagrams of s.

        Args:
            s (str): The source string
            t (str): The target string

        Returns:
            (bool): True if t is an anagram of s,
                False otherwise.
        """
        if len(s) != len(t):
            return False

        letter_counts: dict(str, int) = {}
        for letter in s:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        
        for letter in t:
            if letter in letter_counts:
                if letter_counts[letter] == 1:
                    del letter_counts[letter]
                else:
                    letter_counts[letter] -= 1
            else:
                return False

        return len(letter_counts) == 0
