class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Runtime: O(n)
        Memory: O(26) 
        """
        characters: dict[str, int] = {}
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            characters[char] = 0

        left: int = 0
        right: int = 0
        max_length: int = 0
        
        while right < len(s):
            max_char = max(characters, key=characters.get)
            max_char_count = characters[max_char]
            substitutions_required = right - left - max_char_count

            if max_char_count == 0 or characters[s[right]] == max_char_count or k - substitutions_required >= 1:
                characters[s[right]] += 1
                right += 1
                max_length = max(max_length, right - left)
            else:
                characters[s[left]] -= 1
                left += 1
        return max_length