class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Top down DP approach 
        dp = {}

        def backtrack(i, bought):
            if i >= len(prices): return 0 
            if (i,bought) in dp:
                return dp[(i,bought)]
            res = backtrack(i+1, bought)
            if bought:
                res = max(res, prices[i]+backtrack(i+1, False))
            else:
                res = max(res, -prices[i]+backtrack(i+1, True))
            dp[(i,bought)] = res
            return res
        return backtrack(0, False)