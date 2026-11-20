class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i == n: # This means n == 1, from here we can find that [] is a base case
                        # [1] is n-1 and n-2 is always [1,2] so 1 and 2 ways, while n-3 and so forth
                return 1
            if i > n:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)