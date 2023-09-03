import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # indices
        l = r = 0

        while r < len(nums):
            # collapse rightmost values to maintain monotonically decreasing
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from window if out of bound
            if q[0] < l:
                q.popleft()
            
            # once the window is k elements long, start putting outputs
            if r + 1 >= k:
                output.append(nums[q[0]])

                # update l for next iteration to maintain window length k
                l += 1
            # update r for next iteration to shift window
            r += 1
        
        return output