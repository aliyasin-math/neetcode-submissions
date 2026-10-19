class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if (len(nums) == 3):
            if nums[0]+nums[1]+nums[2]==0:
                return [nums]
            else: 
                return []
        
        nums = sorted(nums)
        res = []

        for i in range(2, len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            target = -nums[i]

            left = 0
            right = i -1

            while left < right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    triplet = [nums[left],nums[right],-target]
                    res.append(triplet)

                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
        return res

        





        
