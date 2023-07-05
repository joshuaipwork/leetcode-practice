class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Memory: O(n * 26), where n is the # of strs
            this is only possible because we know that all the letters are lowercase alphabetical
            if it can be any unicode character, it's O(n * k) where k is the average length 
        Runtime: O(n * k), where n is the # of strs and k is the average length of the strings
        """
        # define data structures
        anagrams: dict[str, list[str]] = {}

        # iterate through each string in strs
        for string in strs:
            # sort the string
            counts = [0] * 26
            for char in string:
                # ord returns an integer representing a characters
                counts[ord(char) - ord("a")] += 1

            # insert into dict
            counts = tuple(counts)
            if counts in anagrams:
                anagrams[counts].append(string)
            else:
                anagrams[counts] = [string]

        return list(anagrams.values())

    def groupAnagramsUnicode(self, strs: list[str]) -> list[list[str]]:
        """
        Memory: O(n * 26), where n is the # of strs
            this is only possible because we know that all the letters are lowercase alphabetical
            if it can be any unicode character, it's O(n * k) where k is the average length 
        Runtime: O(n * k), where n is the # of strs and k is the average length of the strings
        """
        # define data structures
        anagrams: dict[str, list[str]] = {}

        # iterate through each string in strs
        for string in strs:
            # sort the string
            sorted_str = ''.join(sorted(string))

            # insert into dict
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]

        return list(anagrams.values())   