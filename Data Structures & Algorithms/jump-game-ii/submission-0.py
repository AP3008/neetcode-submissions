class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        # We need left and right pointers which we treat as the window our current jump is within 
        l = r = 0
        
        # Think of this as a simplified bfs 
        # While r (the end of the window) is within the list we are still looking for jumps
        while r < len(nums)-1:
            # We want to keep track on each iteration the farthest we can go 
            farthest = 0
            # For every element between l and r we check if that index + the jump value on that index is the farthest. 
            # We are allowed to do this because we know that our window is from the current index to the farthest from the previous iteration
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            # We put l one step ahead of where r was for our new window
            l = r + 1
            # We set r as the farthest because that is the farthest out we can go on this iteration
            r = farthest 
            # We take increment res because this is equal to 1 jump
            res += 1
        # Time: O(n), Space: O(1)
        return res