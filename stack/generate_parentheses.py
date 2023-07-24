class Solution:
    def generateParenthesisRecursive(self, n: int) -> List[str]:
        """
        Memory: O(2^(2n)*n)
        Runtime: O(2^(2n)*n)
        """
        res = []

        def backtrack(string, opens, closes, n):
            if opens == n and closes == n:
                res.append(string)
            if closes < opens:
                backtrack(string + ")", opens, closes + 1)
            if opens < n:
                backtrack(string + "(", opens + 1, closes)
        backtrack("", 0, 0)
        return res

    def generateParenthesisStack(self, n: int) -> List[str]:
        strings = [ ("", 0, 0) ] # (string, opens, closes)
        res = []

        while strings:
            string, opens, closes = strings.pop(-1)
            if opens == n and closes == n:
                res.append(string)
            if closes < opens:
                strings.append((string + ")", opens, closes + 1))
            if opens < n:
                strings.append((string + "(", opens + 1, closes))

        return res
