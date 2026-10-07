class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if n in seen:
                return True
            seen[n] = None
        return False