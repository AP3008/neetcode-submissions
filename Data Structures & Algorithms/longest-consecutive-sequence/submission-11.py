class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sliding window, have a left and right pointer, we track the max length. The right pointer will be incremented via the for loop and we manually chnage the left pointer. We simply check if the value at the right pointer is +1 the value at the right pointer -1, if it is, we continue and increment the length, if it is not we increment the left until it is at the right pointer and then carry on searching, for our max length string. The list must be sorted first. 

        if not nums: return 0 

        l = 0 
        maxLength = 1 
        nums = sorted(list(set(nums)))

        for r in range(1,len(nums)):
            if nums[r] == nums[r-1]+1:
                length = r - l + 1
                maxLength = max(maxLength, length)
            else:
                l = r
        return maxLength 

        # [1,2,10,20]
        # l=0
        # r=1,
        # maxLength = 2 