class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy problem: 

        # If a the amount of gas is less than the cost, a solution doesn't exist
        if sum(gas) < sum(cost):
            return -1 
        
        total = 0
        res = 0 
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            # If our total dips below 0, we know that this starting point doesn't work 
            if total < 0:
                total = 0
                res = i + 1
        return res 