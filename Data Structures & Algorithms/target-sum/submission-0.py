class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for curSum, count in dp.items():
                next_dp[curSum + nums[i]] += count
                next_dp[curSum - nums[i]] += count
            dp = next_dp
        return dp[target]
