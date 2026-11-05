class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Brute force is starting from 0 or 1 you can just sum the cost to see which is cheaper. 

        # DP sol. iterate right to left suing teh input array only storing the two values. We need to append 0 to the array so we can 

        cost.append(0)
        # Starting at the index that comes before the last two because we need the values at n-1 and n-2 of the original cost array, this will be len(cost)-3 because we added 0 to the end as the final platform.   
        for i in range(len(cost)-3,-1,-1):
            # The cost of the current index is the minimum cost of the ways to get there which is the cost at i and the cost of i+1 or i+2 depending if we made a jump of 2, This logic is essentially using the suffix logic.
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2]) 
        return min(cost[0], cost[1])