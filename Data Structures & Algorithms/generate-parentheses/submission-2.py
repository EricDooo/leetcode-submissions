class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string, opens, closes):
            if len(string) == 2*n:
                res.append(string)
                return
            
            if opens < n:
                dfs(string + "(", opens + 1, closes)
            if opens > closes:
                dfs(string + ")", opens, closes + 1)

        dfs("", 0, 0)
        return res