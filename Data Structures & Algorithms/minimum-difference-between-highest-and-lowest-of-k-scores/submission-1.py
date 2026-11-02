class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # IDEA: Sort the list and use a sliding window. The window will be k sized, and since the array is sorted the kth furthest element away from an arbitrary nums[i] will be the optimized minimum, instead of having something really complicated. We just want to explore all of the values to find

        # Left and right pointer, to define our window. 
        l, r = 0, k-1 
        # maximum possible num as our starting point
        res = float('inf')
        # sorting the array so our window logic works
        nums.sort()
        # Since the size of our window isn't changing we are just incrementing the entire winodw 
        while r < len(nums):
            # getting the diff for teh window 
            diff = nums[r] - nums[l]
            # checking if diff is our new min 
            res = min(res, diff)
            # incrementing the window 
            l+=1 
            r+=1 
        # returning the smallest diff we found. 
        return res 