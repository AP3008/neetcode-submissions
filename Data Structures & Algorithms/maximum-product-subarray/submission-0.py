class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # We want to start from the left and keep on multiplying until the end of the array, keeping track of the max value we see, we can do this for every value in the array, since we would see every sub array product that way. This is a brute force sol. and runs O(n^2) but uses O(1) space. 

        # How can we have a better DP solution?

        # 
        # absolute worst case we just include the maximum value of the array because the product with all other elements creates something less     
        res = max(nums)
        # We want to track the current min and max that we have seen in the array so far. 
        curMin, curMax = 1, 1
        # We iterate through the list once 
        for n in nums:
            # If we come across a 0, this messes up our subarrays so we reset it back to 1 for bot mins and maxes 
            if n == 0:
                curMin, curMax = 1, 1
                continue 
            # We store the current max * the value at this index in a temp value incase it changes in the next operation.
            tmp = curMax * n
            # We want to find out if the current max is is the current value, the current value * the current max, or the current min * the current value (because of negative values) 
            curMax = max(curMax * n, n * curMin, n)
            # We do the same thing for the current min, but use the original val for curMax incase it has changed. 
            curMin = min(tmp, n * curMin, n)
            # If the currentMax is greater than the value stored in res, we update res
            res = max(res, curMax)
        # Once the loop finishes we return res, with O(n) Time complexity. 
        return res 
