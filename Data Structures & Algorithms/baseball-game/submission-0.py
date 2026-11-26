class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # We use a stack to append the elements and pop when we see C. to grab the last two elements we can use stack[-1] and stack[-2] if len(stack) >= 2
        stack = []
        for c in operations:
            if c == '+' and len(stack)>1:
                stack.append(stack[-1]+stack[-2])
            elif c == 'C':
                stack.pop()
            elif c == 'D' and stack:
                stack.append(stack[-1]*2)
            else:
                stack.append(int(c))
        return sum(stack)
