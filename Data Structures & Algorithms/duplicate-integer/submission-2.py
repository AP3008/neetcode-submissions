class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True 
            else:
                hash_map[num] = 0
        return False