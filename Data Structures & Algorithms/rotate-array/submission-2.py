class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time: O(n), Space: O(n)
        k = k%len(nums)
        n = len(nums)
        res = [0]*len(nums)
        for i in range(n):
            res[(k+i)%n] = nums[i]
        
        for i in range(n):
            nums[i] = res[i]
        