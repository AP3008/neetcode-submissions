class Solution:
    def isValid(self, s: str) -> bool:
        # There is an idea but this is wrong
        complement = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        if len(s)%2 != 0:
            return False 

        stack = []
        for half in s:
            if half in complement:
                if stack:
                    if complement[half] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(half)
        if stack: return False 
        else: return True 