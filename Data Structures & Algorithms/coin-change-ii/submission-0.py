from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, total) -> int:
            # Base cases
            if total == 0: # This is a valid combination
                return 1
            if i == len(coins):
                return 0
            take = 0
            if coins[i] <= total: # can only take if allowed
                take = dfs(i, total - coins[i])
            skip = dfs(i + 1, total)
            return take + skip	
        return dfs(0, amount)