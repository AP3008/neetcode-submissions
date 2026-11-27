class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The weight capacity is the sum of the max weight brought on one of the days 
        # If the days is the length of the array the answer is the largest element in the array so weight[r]
        # This means that the min capacity is the length of the array. 
        # The upper bound is the sum of the input array. This can be our search space.

        # Our search boundary is between the heaviest weight and the sum of all of teh weights in the worst case 
        l, r = max(weights), sum(weights)
        # Since sum(weights) is our worst case we can set that as the result from the beginning and then try to minimize. 
        res = r 

        # we use this helper function to return a boolean telling us if the day is valid. 
        def canShip(cap):
            # We call them ships but this is meant to be the days. 
            # We know that at minimum we will use 1 ship 
            # We want to have a current capacity that we subtract the weights off to see if we need another ship. 
            ships, currCap = 1, cap
            # We iterate throguh the loop of weights. 
            for w in weights:
                # If teh current cap minus the current weight day we are on is less than zero that ship / day is overflowing so we have to increment the day / ship counter by one and do the operation on the following ship / day. 
                if currCap - w < 0:
                    # Once we increment the ships / day we get a fresh capacity so we can always execute the currCap -= w operation. 
                    ships+=1 
                    currCap = cap
                currCap -= w
            # If the amount of ships / days is equal or less than the days paramenter passed into the function we can return True otherwise we return False. 
            return ships <= days

        # This is our main binary search through the search space. Since we know the answer lies between l and r we can implement an operation to run O(log(r-l))
        while l <= r:
            # cap is our mid point value.
            cap = l+(r-l)//2 
            # If it is true that this value for cap works we can check if it is better than res and shrink the window from teh right searching for a smaller value. 
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            # If it was false, we know that the value for cap was too small so we need to shrink the window from the left side and increase the values in teh search range so we set l to cap + 1 
            else:
                l = cap + 1
        # Once this finishes executing res should store the minimum value that we can find. 
        return res 
        