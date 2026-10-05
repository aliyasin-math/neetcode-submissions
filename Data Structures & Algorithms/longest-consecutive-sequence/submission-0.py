class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = sorted(set(nums))
        lengths = []
        i = 0
        current = [nums[i]]

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1] - 1:
                current.append(nums[i + 1])
                i += 1
            else:
                lengths.append(len(current))
                current = [nums[i + 1]]
                i += 1

        lengths.append(len(current))
        return max(lengths)