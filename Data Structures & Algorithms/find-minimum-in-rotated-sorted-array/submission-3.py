class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0]<nums[-1]:
            return nums[0]
        elif len(nums) == 1:
            return nums[0]
        elif nums[0]>nums[-1]:
            l, r = 0, len(nums)-1

            while l<r:
                mid = (l+r) // 2

                if (nums[mid]>nums[r]) and (nums[mid]>nums[l]):
                    l = mid
                elif (nums[mid]<nums[l]) and (nums[mid]<nums[r]):
                    r = mid 
                elif nums[l]>nums[r]:
                    return nums[r]