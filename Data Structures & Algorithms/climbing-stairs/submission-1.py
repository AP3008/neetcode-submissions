class Solution:
    def climbStairs(self, n: int) -> int:
        # DP problem 
        # Potentially use decision tree and backtracking logic to build up a list of valid solutions and then return the length of the list, but this will be inefficient especially if there is a way to remember work already done. instead of keeping track of the steps taken and popping out the elements, we can just return 1 for a valid path 

        # THIS IS THE BRUTE FORCE SOL. WHICH DOES NOT WORK FOR LARGE N's THIS IS O(2^n)
        #def dfs(i):
        #    if i == n: return 1
        #    if i > n: return 0 
        #    return dfs(i+1) + dfs(i+2)
        
        #return dfs(0)

        # We use a bottom up DP approach where we use a DP array for memoization, remembering / caching the sub problems that we solve. We want to figure out from n how many ways can we get to n then we decrement down so if n = 5, we want to see how many ways from 5 we can get to 5, whcuh is 1, then from 4, it will also be 1, then to find 3 we take the sum of the last 2 that we just figured out, so from 5 and 4 it would be 1+1, which means 3 will have 2 ways, which is true. Then from step 2 we sum 3 and 4 which is 2+1 = 3, and this continues until we get to 0, where our answer is dp[0]

        # this is our intial one and two, ways of getting to n 
        one, two = 1, 1
        # Since we already have our ways from n and n-1, we want to loop from 0 -> n-2
        for i in range(n-1):
            # we store one, so we can set two to it for the next iteration
            temp = one
            # Our new one will be the sum of the previous one and two 
            one = one + two
            # two equals our old temp 
            two = temp
        # return our one as the sum of all ways to get to get to n 
        return one
