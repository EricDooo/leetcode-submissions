class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]

        for r in prices:
            profit = r - buy
            if buy > r:
                buy = r
            maxP = max(maxP, profit)
        return maxP