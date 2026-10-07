class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 1. target = nums[i] + nums[j] => target - nums[j] = nums[i]
        # We can use a hashmap tracking the index and values that we have seen and seeing if we can get a value that we have seen from taking away target from nums[j]
        seen = defaultdict()
        for i in range(len(nums)):
            val = target - nums[i]
            if val in seen:
                return [seen[val], i]
            seen[nums[i]] = i
        return 
