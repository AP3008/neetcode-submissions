class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we want the dp array to be going from 0 to ... amount
        # The default amount+1 because it is a max values, it could be inf 
        dp = [amount+1] * (amount+1) 
        # dp[0] = 0 because we can't use 0 coins 
        dp[0] = 0

        # We loop through all of the values from 1 to amount 
        for a in range(1,amount+1):
            # for each coins in the bag we want to see if there is a coin that will bring us to 0 
            for c in coins:
                if a - c >= 0:
                    # If we get a value of 0 or over, we want to check if the min value is the current value stored or 1 + the coins used to reach the a-c, which would have a value since a-c would have been traversed by this point, and it would have the optimal way to arrive at that square using coins. 
                    dp[a] = min(dp[a], 1+dp[a-c])
        # Once we have all of that, that means the optimal path would be stored in dp[amount] but if dp[amount] is our intial value, then we return -1 because that means there was no path for dp[amount] to be created with any of the solutions. 
        return dp[amount] if dp[amount] != amount + 1 else -1