class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy: From the back of the array we want to see if we are allowed to move the goalpost to the beginning, we can move the goalpost when the current index plus the nums[i] is greater than the index of the goal post because that means some jump can be made to reach the goal post. If that jump can be made we move the goal post to index i. We do this until the goal post equals 0 
        goal = len(nums)-1
        # going backwards through the array 
        for i in range(len(nums)-1,-1,-1):
            # i is where we are jumping from, we can add the jump length to i, and see if there is some jump we can make to reach the goalpost
            if i + nums[i] >= goal:
                # if we can, we can move the goalpost to the current index 
                goal = i
        # We return true if the goalpost is at index 0 otherwise we return false 
        return True if goal == 0 else False 