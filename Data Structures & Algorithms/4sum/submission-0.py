class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # We sort to skip over duplicates 
        nums.sort()
        # res is what we return at the end 
        # quad is our current array of quadruplets that we are storing
        res, quad = [], []
        # we use a recursive function that lets us calculate the sum for any target needing k values to sum up to it. 
        # k = the length of the final list 
        # start = the starting index 
        # target = the target value we want to find, we are masking the above target because target within kSum will change dynamically as we recurisvely call the function.
        def kSum(k, start, target):
            # If k does not equal two meaning we have 4 or 3 values left to find, we want to for every value in the array call the function again so that we can then implement the 
            if k != 2:
                # We take len(nums)-k+1 because we need to make sure that there are at least k values left to explore. 
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    # This is a similar backtracking technique of appending then popping once the dfs finishes.
                    quad.append(nums[i])
                    kSum(k-1, i+1,target-nums[i])
                    quad.pop()
                # We return to not execute the remaining code on a k > 2
                return 
            # We implement a two pointer solution where we use the fact that nums is sorted as an optimal way to find two values that sum to target. 
            l, r = start, len(nums)-1
            # We use l<r because we cannot have overalapping values. 
            while l < r:
                # if teh sum of the two pointers is less than the target we increment the left pointer because we know in a sorted array that will get us a larger value. 
                if nums[l] + nums[r] < target:
                    l+=1
                # If it is greater we want to decrease the right pointer to get a smaller value. 
                elif nums[l] + nums[r] > target:
                    r-=1
                # If they are equal we want to add what is in quad and the left and right pointer.
                else:
                    res.append(quad+[nums[l],nums[r]])
                    # We arbiteraily increment the left pointer 
                    l+=1 
                    # since we want to skip over duplicates we have to loop the increment if the previous values at nums[l] matches the newly incremented one. 
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        # Since the problem is 4Sum we have to use 4 as the value for k, we start at index 0, and the traget is the targte that is passed into the question. 
        kSum(4,0,target)
        # Once kSum executes we can return res as it will be populated with the solutions. 
        return res