class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # IDEA: We want to think of it as a decision tree where we can choose to add a parethese or close it off. We keep track of the amount of open and closed parentheses and when the equal the n we can append the string to our result list 

        # We keep track of teh string in a stack and join it later on a string when appending 
        stack = []
        # Our resulting array 
        res = []

        # Our backtrack function that handles the decision to be made. 
        def backtrack(openN, closedN):
            # If open and closed equal n we want to add this combination to our result 
            if openN == closedN == n:
                # We have to use "".join() because we are keeping track via a stack 
                res.append("".join(stack))
            # If the amount of open parentheses is less than n we can add another one to the list
            if openN < n:
                # we add an open bracket to the stack and run the function again with the open counter incremented
                stack.append("(")
                backtrack(openN+1, closedN)
                # we remove the open parenthese so we can explore what happens if we close the previous parenthese if the amount of closed parentheses is less than open 
                stack.pop()
            if closedN < openN:
                # adding a closed bracket and running the function again, but with the closed counter incremented. 
                stack.append(")")
                backtrack(openN, closedN+1)
                # removing the closed bracket off our stack to not intefere with the subsequent recursive calls
                stack.pop()
        # calling the function from the beginning with nothing built up 
        backtrack(0,0)
        # returning our resulting list. 
        return res 