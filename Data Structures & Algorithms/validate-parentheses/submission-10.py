class Solution:
    def isValid(self, s: str) -> bool:
        # Have a matching hashmap connecting each parenthese to it's closing variant,we use a stack to push all of the open parentheses and when we encounter a closed variant we pop off the stack to see if it is being closed in order. 
        if len(s) % 2 == 1: return False
        stack = []
        par = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for p in s:
            if p not in par: # Not a key in the stack means it is an open bracket 
                stack.append(p)
            else:
                if not stack: return False 
                brac = stack.pop()
                if brac != par[p]: return False 
        return not stack 