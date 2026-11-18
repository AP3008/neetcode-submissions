class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Time: O(n), Space: O(1)
        count = defaultdict(int)
        for n in nums:
            count[n]+=1 
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1: # We create a new dict, so it is easier to remove a key, so instead of deleting the key we create a new hashmap that will at most have 2 elements. 
                    new_count[n] = c - 1
            count = new_count

        res = []
        # even though this seems linear time, it will only have at most n elements. 
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res