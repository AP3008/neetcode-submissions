class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start of the array is a number that does not have nums[i]-1 in it 
        #res = 0
        #nums.sort()

    #    curr, streak = nums[0], 0
     #   i = 0
      #  while i < len(nums):
       #     if curr != nums[i]:
        #        curr = nums[i]
         #       streak = 0
          #  while i < len(nums) and nums[i] == curr:
           #     i+=1
            #streak += 1 
            #curr += 1
            #res = max(res, streak)
        #return res 

        numSet = set(nums)
        longest = 0
        length = 1
        for num in numSet:
            if num-1 in numSet:
                length = 1
                continue 
            while length < len(numSet) and num+length in numSet:
                length+=1
            if longest < length:
                longest = length
        return longest 