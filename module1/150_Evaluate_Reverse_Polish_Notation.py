class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isOperator(token):
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                result = self.operations(token, val1, val2)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]
    
    def isOperator(self, token):
        if token in '+*/-':
            return True
        return False
    
    def operations(self, token, val1, val2):
        if token == '+':
            return val1 + val2
        elif token == '-':
            return val2 - val1
        elif token == '*':
            return val1 * val2
        elif token == '/':
            return int(val2 / val1)
        else:
            return 0

