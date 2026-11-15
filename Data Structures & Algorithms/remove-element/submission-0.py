class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # We essentially want to swap all of the values that match val to the end of the array. We iterate through the array keeping track of k, which will increment for all of the values not matching val. If we come across a value that matches val we skip it and don't touch k because now for the next non-val value we find we want to swap it's places. So k will always be slower than i if there are val's matching in the array. 
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k  
        