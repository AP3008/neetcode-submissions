class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # IDEA: Think of a decision tree where we can choose to keep a number or not. If we decide to keep the number we stay on the same index and add it to the total to see if we got a hit. if we choose not to keep the number we increment the index by 1 moving on to the next number. 

        # Creating our result array outside of the function. 
        res=[]
        # A DFS that takes in the index which maps to a place in nums, the curr arary which is the numbers that we have in a set now, and total the total sum of the current array, not to waste operations on calculating the sum each time. 
        def dfs(i, curr, total):
            # If the total of the current array equals the target, we want to include it in the resulting array 
            if total == target:
                res.append(curr.copy())
                return 
            # If the index is outside of nums, we discontinue the dfs, if target is too large we also discontinue the dfs because this subset will not generate a valid answer. 
            if i >= len(nums) or total > target:
                return 
            # We want to add the value at nums[i] and go through the dfs again to see if we have a set that sums to target.
            curr.append(nums[i])
            # We continue at the same index because we need to make the decision to keep or not to keep the value when we run the dfs again. 
            dfs(i, curr, total+nums[i])
            # We pop off the current element because we are not including in the other decision route we are going down.
            curr.pop()
            # We increment the index because we are choosing not to include this number. 
            dfs(i+1, curr, total)
        # We start the dfs from an empty list and index 0 
        dfs(0,[],0)
        # We return the result because all of the lists will added after the dfs is complete. 
        return res 