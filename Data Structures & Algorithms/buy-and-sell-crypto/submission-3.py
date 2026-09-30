class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy = prices[0]

        for r in range(1,len(prices)):
            if buy > prices[r]:
                buy = prices[r]
            profit = prices[r] - buy
            maxprofit = max(maxprofit, profit)
        
        return maxprofit