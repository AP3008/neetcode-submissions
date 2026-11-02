class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # IDEA: Sort the list and use a sliding window. The window will be k sized, and since the array is sorted the kth furthest element away from an arbitrary nums[i] will be the optimized minimum, instead of having something really complicated. We just want to explore all of the values to find

        l, r = 0, k-1 
        res = float('inf')
        nums.sort()
        while r < len(nums):
            diff = nums[r] - nums[l]
            res = min(res, diff)
            l+=1 
            r+=1 
        return res 