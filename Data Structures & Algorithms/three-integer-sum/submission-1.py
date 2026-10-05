class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i + j + k = 0
        # j + k = -i

        # 1. Sort the list

        nums.sort() 
        res = []
        for i in range(len(nums)):
            # 2. If the number has already been seen we want to skip it
            # This works because in a sorted list the last value would be the same value
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            l, r = i + 1, len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val > 0:
                    r-=1
                elif val < 0:
                    l+=1  
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1 
        return res