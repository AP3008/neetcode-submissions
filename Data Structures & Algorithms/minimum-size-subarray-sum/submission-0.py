class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Subarray means we can use a sliding window.
        # We can't just return a subarray with a sum greater thna target we also need to find the smallest one. 
        # We want to test each subarray with a sum greater than target and store it. 

        res = float('inf')
        l = 0
        curr = nums[0]
        if curr >= target: return 1
        for r in range(1,len(nums)):
            curr += nums[r]
            while curr >= target:
                res = min(res, r-l+1)
                curr-=nums[l]
                l+=1 
        return res if res != float('inf') else 0  

            