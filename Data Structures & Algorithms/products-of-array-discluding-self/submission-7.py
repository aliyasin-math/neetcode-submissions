class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        left = 1
        right = 1

        for i in range(len(nums)):
            res[i] = left
            if i < len(nums) -1:
                left *= nums[i]

        for i in range(len(nums)):
            res[len(nums) - i-1] *= right
            if i < len(nums) -1:
                right *= nums[len(nums) - i-1]
        
        return res
        