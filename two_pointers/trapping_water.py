class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0
        # let max_left[i] be the maximum of all elements in h with indices < i
        # let max_right[i] be the maximum of all elements in h with indices > i
        # let water[i] be the amount of water that can be stored at index i

        # water[i] = max(0, min(max_left[i], max_right[i]) - h[i])

        # max_left[i] >= max_left[j] if j < i
        # max_right[i] >= max_right[j] if j > i

        # let l <= r
        # if you know max_left[l] and that max_right[r] >= max_left[l], then water[l] = max_left[l] - h[l]
        # if you know max_right[r] and that max_left[l] >= max_right[r], then water[r] = max_right[r] - h[r]

        l = 0
        r = len(h) - 1
        max_left = 0 # the max of elements in h with index < l
        max_right = 0 # the max of elements in h with index > r
        water = 0

        while l <= r:
            if max_left <= max_right:
                water += max(0, max_left - h[l])
                max_left = max(max_left, h[l])
                l += 1
            else:
                water += max(0, max_right - h[r])
                max_right = max(max_right, h[r])
                r -= 1
        
        return water
