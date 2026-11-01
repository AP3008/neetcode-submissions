class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # IDEA: Same as combinations sum but instead of staying at the same index and not incrementing when we choose that value we, always inrement the index up. So we walk down the same decision tree: we choose the number and perform dfs, or we choose 

        res = []
        candidates.sort() 

        def dfs(i, curr, total):
            if total == target and not (curr in res):
                res.append(curr.copy())
                return 
            if i >= len(candidates) or total > target:
                return 
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1 
            dfs(i+1, curr, total)
        
        dfs(0,[], 0)
        return res 