class Solution:
    def findMin(self, nums: List[int]) -> int:
        # From the left side the first time we encounter a number less than the number to it's left it would be the minimum. We can trivially just increment to find this number relativley fast. Though there maybe a better soluton by quickly finding inflextion point using binary search. 
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break 
            m=(l+r)//2
            res=min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m+1 
            else:
                r=m-1
        return res
