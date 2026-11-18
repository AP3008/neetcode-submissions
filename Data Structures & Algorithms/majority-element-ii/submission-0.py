class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Create a hash map counter
        # create a frequency list of size n+1 with lists as elements 
        # Put the frequency as the index and the element appned it to the array at that index. 
        # Then iterate backwards therough the frequency list checking if the index is greater or equal than n//3

        ctr = {}
        for i in range(len(nums)):
            ctr[nums[i]] = ctr.get(nums[i], 0) + 1
        
        freq = [[] for _ in range(len(nums)+1)]
        for key, value in ctr.items():
            freq[value].append(key)
        
        limit = len(nums)//3
        res = []
        for i in range(len(freq)-1,-1,-1):
            if i > limit:
                for n in freq[i]:
                    res.append(n)
            else:
                break 
        return res 