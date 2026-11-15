class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Majority always exists (n//2)
        # We can have a hashmap ctr whichever element has the most occurneces by the time we are done looping, is the majority element. 
        n = len(nums)//2
        ctr = {}
        # Works because array list always empty
        maj = nums[0]
        for n in nums:
            ctr[n] = ctr.get(n,0)+1
            if ctr[n] > ctr[maj]:
                maj = n 
        return maj 
        