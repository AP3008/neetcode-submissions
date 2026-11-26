class Solution:
    def simplifyPath(self, path: str) -> str:
        # We append each directory / file, that lies between two '/ ... /' then we want to pop the last element that follows .. , when we seen a sole . , we can skip it because it refers to current directory.
        # We can ignore '/' when we see them only collecting chars, that are valid in unix. 

        stack = [] 
        s = ""
        for c in path:
            if c == "/":
                if s == "..":
                    if stack:
                        stack.pop()
                    s = ""
                    continue
                elif s == ".": 
                    s = "" 
                    continue  
                elif s != "": 
                    stack.append(s)
                    s = ""
                continue 
            s = s + c
        if s:
            if s == "..":
                stack.pop()
            elif s == ".":
                pass
            else:
                stack.append(s)
        return "/"+"/".join(stack)
         
