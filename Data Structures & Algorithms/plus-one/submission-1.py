class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[-1] += 1
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] >= 10:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    continue
                digits[i-1] += 1
                digits[i] = 0
        return digits
        