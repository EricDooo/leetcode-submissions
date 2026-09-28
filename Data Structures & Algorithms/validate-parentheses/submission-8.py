class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {'}':'{', ')': '(', ']': '['}

        for c in s:
            if c in parens:
                if stack and stack[-1] == parens[c]:
                    stack.pop()
            else:
                stack.append(c)

        return True if not stack else False