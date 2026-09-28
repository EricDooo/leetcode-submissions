class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])

        for tok in tokens:
            
            if tok not in ops:
                stack.append(int(tok))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if tok == '+':
                    stack.append(val1 + val2)
                elif tok == '-':
                    stack.append(val1 - val2)                
                elif tok == '*':
                    stack.append(val1 * val2)
                elif tok == '/':
                    print(val1, val2)
                    stack.append(int(val1 / val2))
        return stack[0]