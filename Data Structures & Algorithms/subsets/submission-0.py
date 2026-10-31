class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # IDEA: We can think of the problem as a decision tree. For each number in the list we can think to include or exclude it from the set. 2 choices for every element on a n-length array. this means we have 2^n different subsets. We can think of this as a decision tree where we use each element as a decision node to keep or not keep the element. The heigh corresponds to the number of elements in nums and the last row where all decisions have been made will be our resuslting list of subsets. We can implement this using a DFS and exploring the DFS of each decision. 
        
        # Resulting array where we add each subset to 
        res = []

        # We want to intialize it outside of the function because we don't want to have to pass in a list every time we call dfs instead we can use one that tracks all of our subsets.
        subset = []
        # Index is the current element that we are visiting 
        def dfs(i):
            if i >= len(nums):
                # We add a copy of subset because python appends the reference to the list so it will change values if we modify subset, which we don't want
                res.append(subset.copy())
                # We can end our dfs search once all elements of the array are traversed 
                return 
            # decision to include nums[i]
            # Then we increment the index counter for the next dfs 
            subset.append(nums[i])
            dfs(i+1)

            #decision NOT to include nums[i]
            # This is so that when we call dfs again we don't include nums[i] in that subset, then call dfs again. If the index goes out of range we return whatever is in subset. 
            subset.pop()
            dfs(i+1)
        # Starting from index 0 we build up every subset.
        dfs(0)
        # return the result, it isn't in any order, but rather how the recursive function builds it, the empty set will be last added because of how the function is built. 
        return res
            
