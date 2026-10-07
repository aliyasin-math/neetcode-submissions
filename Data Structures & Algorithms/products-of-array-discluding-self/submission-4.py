class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        index_zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                index_zeros.append(i)
        
        if len(index_zeros) > 1:
            return res
        elif len(index_zeros) == 1:
            result = 1
            for j in range(len(nums)):
                if j!=index_zeros[0]:
                    result *= nums[j]
            res[index_zeros[0]] = result
            return res
            


        left = 1
        right = 1
        for i in range(1,len(nums)):
            right *= nums[i]
        for i in range(len(nums)):
            res[i] = int(left*right)
            if i < len(nums) -1:
                left *= nums[i]
                right /= nums[i+1]
        return res
        