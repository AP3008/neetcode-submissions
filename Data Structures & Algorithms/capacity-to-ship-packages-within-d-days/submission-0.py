class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The weight capacity is the sum of the max weight brought on one of the days 
        # If the days is the length of the array the answer is the largest element in the array so weight[r]
        # This means that the min capacity is the length of the array. 
        # The upper bound is the sum of the input array. This can be our search space.

        l, r = max(weights), sum(weights)
        res = r 

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships+=1 
                    currCap = cap
                currCap -= w
            return ships <= days

        
        while l <= r:
            cap = l+(r-l)//2 
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res 
        