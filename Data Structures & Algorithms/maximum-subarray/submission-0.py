class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       #
        # This is our current max value, the first element of the arrat
        maxSub = nums[0]
        # The current sum is what we will be constantly recalculating and comapring to our max to see if we got a larger value.
        curSum = 0
        # We want to iterate through the list 
        for n in nums:
            # If our currentSum (prefix of the current value) is less than zero we can disregard it, and essentially slide our window to the current value of nums, forgetting the previous value 
            if curSum < 0:
                curSum = 0
            # we add n to the current sum and then compare the value to the largest value we have seen 
            curSum += n
            maxSub = max(maxSub, curSum)
        # We return the maxSubarray 
        return maxSub
