class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        # We push tokens onto the stack until we see an operand, once we see an operand we perform that operation, then push the result back onto the stack, and continue the same way. This way we still preserve the values for future uses, if we were to push more numbers on to the stack. 

        stack = []
        for c in tokens:
            if c not in operators:
                stack.append(c)
            else:
                v2 = int(stack.pop())
                v1 = int(stack.pop())
                if c == "+":
                    stack.append(v1+v2)
                elif c == "-":
                    stack.append(v1-v2)
                elif c == "*":
                    stack.append(v1*v2)
                else:
                    stack.append(int(v1/v2)) # using truncate, because we are using only int's 
        return int(stack.pop())