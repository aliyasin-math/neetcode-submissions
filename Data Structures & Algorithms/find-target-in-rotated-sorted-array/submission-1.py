class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r) // 2

            if nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            elif nums[mid] == target:
                return mid

            if nums[mid]<target:
                if (nums[mid]<nums[r]) and (nums[r]<nums[l]) and (nums[l]<target):
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid]>target:
                if (target<nums[r]) and (nums[r]<nums[l]) and (nums[l]<nums[mid]):
                    l = mid+1
                else:
                    r = mid-1

        return -1
            
        