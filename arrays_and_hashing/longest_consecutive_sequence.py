class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Memory: O(n)
        Runtime: O(n)
        """
        # put everything into a set
        ints: set[int] = set(nums)
        max_len = 0

        # look for consecutive sequences in the set, updating length as we find
        # longer chains
        while ints:
            # pops some element from the set
            start = ints.pop()
            len = 1
            preceding = start - 1
            following = start + 1

            # check if subsequent or preceding elements are in the set, updating length
            while preceding in ints:
                len += 1
                ints.remove(preceding)
                preceding -= 1
            while following in ints:
                len += 1
                ints.remove(following)
                following += 1
            max_len = max(max_len, len)
        
        return max_len