class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in seen:
                return [seen[v], i]
            seen[nums[i]] = i
