class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for x in nums:
            if x in seen:
                return True
            seen[x] = None
        return False