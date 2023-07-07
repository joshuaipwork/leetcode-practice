class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer: list[int] = [1] * len(nums)
        suffix: int = 1

        # populate answer with prefixes
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        # for each prefix, starting from the back
        for i in range(len(nums) - 1, -1, -1):
            # multiply prefix by suffix
            answer[i] *= suffix
            # multiply suffix by corresponding num as we move
            suffix *= nums[i]

        return answer 