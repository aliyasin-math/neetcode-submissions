class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if nums[0]+nums[1]+nums[2]==0:
                return [nums]
            else:
                return []

        nums = sorted(nums)
        res = []

        for i in range(2,len(nums)):
            left = 0
            right = i-1
            while left < right:
                if nums[left]+nums[right] > -nums[i]:
                    right -= 1
                elif nums[left]+nums[right] < -nums[i]:
                    left += 1
                else:
                    triplet = (nums[left], nums[right], nums[i])
                    res.append(triplet)
                    left += 1
                    right -= 1
        return list(set(res))





        
