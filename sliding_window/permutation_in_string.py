class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # def data structures
        letters_required: dict[str, int] = {}
        counter: int = 0

        # insert all the letters from s1
        for letter in s1:
            # account for first time we see the letter
            if letter not in letters_required:
                letters_required[letter] = 0
            
            letters_required[letter] += 1
            counter += 1
        
        # use a sliding window algorithm to evaluate each substring
        left: int = 0
        right: int = 0
        # while we haven't checked the whole string
        while right < len(s2):
            # if substring is too short, expand interval to right
            if right - left < len(s1):
                right += 1
                letter_added = s2[right - 1]
                # when expanding interval, update dict and counter
                if letter_added in letters_required:
                    letters_required[letter_added] -= 1
                    if letters_required[letter_added] >= 0:
                        counter -= 1
            # if substring is too long, expand interval to left
            else:
                left += 1
                letter_removed = s2[left - 1]
                # when contracting interval, update dict and counter
                if letter_removed in letters_required:
                    letters_required[letter_removed] += 1
                    if letters_required[letter_removed] > 0:
                        counter += 1

            # if counter == 0, True
            if counter == 0:
                return True

        # otherwise return False
        return False

            