class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Replace original negatives with 0, so it doesn't crowd the values when we turn them negative. 
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        # We mark the numbers that exist as negative, and then check the index of the absolute value of the number at i, Then if that index appears we turn it negative. 
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -(len(nums)+1)
        # We want to find the first position that is not marked and return that number. This works because if all of the numbers are greater than the length of the array we return 1, which is the first positive index.
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        # If every number is marked we want to return the length of the array + 1.  
        return len(nums)+1
            
