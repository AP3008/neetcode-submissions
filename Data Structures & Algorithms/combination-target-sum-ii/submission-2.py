class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # IDEA: Same as combinations sum but instead of staying at the same index and not incrementing when we choose that value we, always inrement the index up. So we walk down the same decision tree: we choose the number and perform dfs, or we choose not to include. Since there are duplicates it is likely we will see the same result trying to be appended to our list. We can deal with this by sorting the list, and running a while loop within our dfs to increment i when we come across a value that is the same as the current one, in an effort to skip past it. 

        # Getting our res array and sorting the candidates. 
        res = []
        candidates.sort() 

        # Our dfs which takes the index, our current array, and the total sum as for now. 
        def dfs(i, curr, total):
            # If we find a subset that works and it is not already in the resulting array we can add it to the list. 
            if total == target and not (curr in res):
                res.append(curr.copy())
                return 
            # If the index is greater than the candidates or total surpasses the target, we want to end the dfs. 
            if i >= len(candidates) or total > target:
                return 
            # Our first decision is to use the current element
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            # Second decision is to skip the current element and all of its potential duplicates. 
            curr.pop()
            # Increment i until we find a new value. 
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1 
            # dfs excluding the value at candidates[i] and all duplicates of it. 
            dfs(i+1, curr, total)
        # calling the dfs from index 0  
        dfs(0,[], 0)
        # returning the result string. 
        return res 