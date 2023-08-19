class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # create data structures
        counter = 0
        l = 0
        r = 0
        char_counts = dict()
        min = ""
        min_len = len(s) + 1

        # insert all the characters in t into char counts
        for char in t:
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1
            counter += 1
        
        # slide the window until we reach the end
        while True:
            # if the window contains t
            if counter <= 0:
                # contract the window from the left
                removed_char = s[l]
                if removed_char in char_counts:
                    if char_counts[removed_char] >= 0:
                        counter += 1
                    char_counts[removed_char] += 1
                l += 1
                
            # if the window doesn't contain t
            else:
                r += 1
            
                if r == len(s) + 1:
                    break

                # expand the window from the right
                added_char = s[r - 1]
                if added_char in char_counts:
                    if char_counts[added_char] > 0:
                        counter -= 1
                    char_counts[added_char] -= 1
            
            # check if the window contains t
            if counter <= 0 and (r - l) < min_len: 
                # if so, update min if shorter
                min_len = r - l
                min = s[l:r]

        # return min
        return min
        