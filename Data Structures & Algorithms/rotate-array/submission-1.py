class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We want to reverse the array and then reverse teh first k elements within the reversed array, and then reverse the leftover len(nums)-k elements. This is O(n) time, O(1) space

        k = k %len(nums)
        if k == 0: return 
        l, r = 0, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1 
            r-=1
        
        l,r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1 
            r-=1
        l = k
        r = len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1 
            r-=1
        
