class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # backtracking solution - brute force
        # think decision tree, in the following sequence we can choose to keep or not keep a value. 

        # DP sol.
        # Top down appraoch, starting at the end we know the longest subsequence is 1, we can work backwards by finiding what choices they can make
        
        # list of Longest subsequences at each value in nums, we leave a 1 there as it is empty 
        LIS = [1] * len(nums)

        # We want to iterate through the list backwards, because it is easier to find the longest subsequence that way. 
        for i in range(len(nums)-1,-1,-1):
            # From i + 1 to the end of the array we loop again 
            for j in range(i + 1, len(nums)):
                # If the number at i is less than the number at j, meaning that we are checking if it is valid for the increasing subseqeunce
                if nums[i] < nums[j]:
                    # This decides whether we are talking j or not. On the first iteration this will be comapring (1, 1+1) since the value at each array is 1 if you take it and 1 more if we include the value we are at. Then we store that is LIS[i] as the current max value that we have seen. This loops for each value from i to j so we can slowly build up the largest sequqence 
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        # By the end the entire DP array will be full of the longest subsequences from each index, and we just want to take the max of that to get the maximum length. 
        return max(LIS)
