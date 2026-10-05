class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(st, opens, closes):
            if len(st) == 2*n:
                nonlocal res
                res.append(st)
                return
        
            if opens < n:
                generate(st+"(", opens + 1, closes)
            if opens > closes:
                generate(st+")", opens, closes + 1)
        generate("", 0, 0)
        return res
            