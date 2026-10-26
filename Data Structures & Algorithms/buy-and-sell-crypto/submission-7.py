class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r]-prices[l]
                max_profit = max(profit, max_profit)
                r += 1
            else:
                l = r
        return max_profit