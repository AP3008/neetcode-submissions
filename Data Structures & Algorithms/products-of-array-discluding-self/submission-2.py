class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can use a prefix list which keeps track of all of the values multiplied before this value has been seen, and a suffix list which keeps track of all of the values multiplied after this value. 

        n = len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = 1
        suffix[n-1] = 1
        for i in range(1, n):
            # This works because the previous value will store all of the previous values multiplied by each other, so all we need to do is multiply the previous indexes value onto it and store it in the ith index 
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            # Starting from the end of the list, but we already have a value at n-1 (1) always, so we start at n-2 and decrement down. So the value of n-2 will be n-1 * nums[i+1](nums[n-1] for first iteration) so we can get all of the values that come after index i.
            suffix[i] = suffix[i+1]*nums[i+1]
        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])
        return res 