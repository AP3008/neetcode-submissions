class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in seen:
                return [seen[value], i]
            seen[nums[i]] = i
