class Solution:
    def findMin(self, nums: List[int]) -> int:
        # let 0 <= r < len(nums) the number of times the array was sorted.
        # nums[r] == min
        # binary search to find r

        # take the whole array of nums as the range
        min_r = 0
        max_r = len(nums) - 1

        while min_r < max_r:
            # covers the case that the array was rotated len(nums) * n times
            if nums[min_r] < nums[max_r]:
                r = min_r
                break

            # take the midpoint of the range
            mid_r = (min_r + max_r) // 2
            # if the number at the midpoint is greater than the left side of the range,
            # then 
            if nums[mid_r] >= nums[min_r]:
                min_r = mid_r + 1
            # if the number at the midpoint is less than the  
            else:
                r = mid_r
                max_r = mid_r - 1
        
        # use this r to find the min
        return nums[r]
