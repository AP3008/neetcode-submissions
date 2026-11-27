class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target: return True 
            if nums[l] < nums[m]: # Left portion is sorted 
                if nums[l] <= target < nums[m]: # If target is within the sorted window
                    r = m - 1
                else: # If it is not we switch the sides we are searching. 
                    l = m + 1
            elif nums[l] > nums[m]: # Right portion is sorted 
                # If nums[m] < target <= r, we know it is in this sorted window so we search there 
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # otherwise the right portion is not sorted and we need to explore the otehr side. 
                else:
                    r = m - 1
            # If any other case comes up that means we are on a duplicate value of nums[m] == nums[l] in that case we want ot increment until there is a non matching l. 
            else:
                l += 1
        return False 