class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0": # Cant start with zero
                return 0

            res = dfs(i + 1) # Decode one digit
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] < '7'
            ):
                res += dfs(i + 2) # Decode both
            dp[i] = res
            return res

        return dfs(0)