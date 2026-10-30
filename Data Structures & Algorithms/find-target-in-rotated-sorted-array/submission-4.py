class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        # Perform regular binary search but we need to find out which side of the rotation we are on. 
        # First: Check if mid is teh target, if so return mid 
        # 2nd: Check if mid is >= nums[left] if so we know that the values from left to mid are ascending. Now we need to find out if target is between nums[left] <= target < nums[mid] If it is we want to make the right index = mid - 1, if it isn't we know target is on the right side of mid if it exists, meaning we move the left index to = mid + 1
        # Last: If the nums[mid] < nums[left] It means that means the values right of nums[mid] are ascending and sorted. So we want to check if target falls between nums[mid] < target <= nums[right]. If it is then we move the left pointer up to mid + 1, if it isn't we need to search left by moving ing the right pointer to mid - 1

        # less than or equal to incase l and r converge on target 
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif nums[m] >= nums[l]:
                # left -> mid is sorted
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1 
                else:
                    r = m-1
        return -1
