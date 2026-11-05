class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # IDEA: have a frequency hashmap, then create a frequency list with the indexes being the amount of times it showed up in the program. We then iterate through the list backwards. This runs through the list of n elements 3 times worst case, meaning that we can say we have O(n) time complexity 
        seen = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        
        freq = [[] for i in range(len(nums)+1)]  
        for key in seen:
            freq[seen[key]].append(key)
        
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                k-=1 
                if k == 0:
                    return res 
        return res     
            



        