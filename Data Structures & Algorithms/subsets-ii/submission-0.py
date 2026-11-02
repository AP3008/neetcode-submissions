class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
       # Use decision, tree choosing to include or not to include, just make sure that if a subset is already in the array we don't put it in. [1,2] and [2,1] are considered the same subset so we need a way to ignore that. We can do this by sorting the list and handling it in the same way as 3sum 
        if len(nums) == 0: return [[]]
        res = []
        nums.sort()
        def dfs(i, curr):
            if i >= len(nums):
                if not(curr in res):
                    res.append(curr.copy())
                return 
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1 
            dfs(i+1, curr)
        dfs(0,[])
        return res 

            
