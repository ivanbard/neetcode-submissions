class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # return the final result of the expression
        # reverse polish notation: 
        # 3 + 4 is now 3 4 + in RPN

        stack = []
        operators = {"+", "-", "*", "/"}

        # go through tokens, push numbers and collapse the last two values
        # whenever an operator appears
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(int(left / right))

        return stack[-1]