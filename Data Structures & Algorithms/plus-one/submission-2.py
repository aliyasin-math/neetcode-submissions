class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)):
            digits[i] = str(digits[i])
        digits = int("".join(digits))
        digits += 1
        digits = list(str(digits))
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        return digits
        