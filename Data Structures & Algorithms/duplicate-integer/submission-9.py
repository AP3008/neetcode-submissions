class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hash map that tracks if a value has been seen 
        seen = {}
        for n in nums:
            if n in seen:
                return True 
            seen[n] = True 
        return not True