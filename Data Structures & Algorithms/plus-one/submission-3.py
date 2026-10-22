class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        def f(x):
            if len(x) == 0:
                return [1]
            elif x[-1] < 9:
                x[-1] += 1
                return x
            else:
                return f(x[:-1]) + [0]

        return f(digits)
        