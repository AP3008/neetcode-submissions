class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Hashset tracking what has been seen so far. If a number appears in the set we want to swap it with the next sequential spot to put it. We can use two pointers for this. One to scan through the element and the other that tells us where to put the value. 
        sett = set()
        l = 0
        for i in range(len(nums)):
            if nums[i] not in sett:
                nums[l] = nums[i]
                l+=1 
            sett.add(nums[i])
        return l 

        