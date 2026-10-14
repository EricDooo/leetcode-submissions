class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(st, opens, closes):
            if len(st) == 2*n:
                res.append(st)

            # Open
            if opens < n:
                backtrack(st + '(', opens+1, closes)
            
            if closes < opens:
                backtrack(st + ')', opens, closes+1)
        backtrack("",0,0)
        return res
