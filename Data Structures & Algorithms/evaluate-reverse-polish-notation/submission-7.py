class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+", "-", "*", "/"
        }
        stack = []
        for i in tokens:
            if i in operations:
                num1 = stack.pop()
                num2 = stack.pop()
                curr = 0
                if i == "+":
                    curr = num2 + num1
                elif i == "-":
                    curr = num2 - num1
                elif i == "*":
                    curr = num2 * num1
                else:
                    curr = int(float(num2)/num1)
                stack.append(curr)
            else:
                stack.append(int(i))
        return stack[0]