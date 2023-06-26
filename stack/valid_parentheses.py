class Solution:
    def isValid(self, s: str) -> bool:
        """
        Memory: O(n)
        Runtime: O(n)

        Determines if the string has valid parentheses.

        Args:
            s (str): A string consisting of only the characters '(', ')', '[', ']', '{', '}'
        Returns:
            (bool): True if 
                Open brackets must be closed by the same type of brackets.
                Open brackets must be closed in the correct order.
                Every close bracket has a corresponding open bracket of the same type.
                False otherwise.
        """
        stack: list[str] = []
        starters = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        enders = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for char in s:
            if char in starters:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != enders[char]:
                    return False
                stack.pop(-1)

        return len(stack) == 0