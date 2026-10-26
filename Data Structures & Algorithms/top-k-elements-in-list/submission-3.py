class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        seen = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1

        for key in seen:
            bucket[seen[key]].append(key)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                if k == 0:
                    break 
                res.append(num)
                k-=1 
        return res
        
