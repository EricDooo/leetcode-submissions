class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            
            if tok not in "+-*/":
                stack.append(int(tok))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if tok == '+':
                    stack.append(val1 + val2)
                elif tok == '-':
                    stack.append(val2 - val1)                
                elif tok == '*':
                    stack.append(val1 * val2)
                elif tok == '/':
                    stack.append(int(val2 / val1))
        return stack[0]