class Solution:
    def rob(self, nums: List[int]) -> int:
        # First house and last house are neighbours so this changes the logic for handling the edges, but we can reuse the logic for the inside poriton? 

        # IDEA: we want to find utilize the same idea from house robber but starting from index 1 and and index 0, meaning for the one at index 1 we include the full array and for index 0 we exclude the end of the array. If the array is of length 1, we just want to check if the nums[0] would return the max. 
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self,nums):
        rob1, rob2 = 0, 0

        for n in nums:
            tmp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2