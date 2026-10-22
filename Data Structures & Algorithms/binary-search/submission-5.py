class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l<=r:
            half_index = math.floor((r+l) // 2)
            if target > nums[half_index]:
                l = half_index + 1
            elif target < nums[half_index]:
                r = half_index -1
            else:
                return half_index
        return -1
