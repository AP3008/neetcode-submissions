class Solution:
    def trap(self, height: List[int]) -> int:
        # 
        # Base-case: returning a 0 if there are no heights in the list 
        if not height: return 0 

        # Creating a left and right pointer at the beginning and end of the array 
        l, r = 0, len(height)-1
        # The current leftMax and rightMax would be the left and right boundaries 
        leftMax, rightMax = height[l], height[r]
        # This is where we store the result
        res = 0
        # While the left pointer doesn't pass the right pointer we loop through the heights 
        while l < r:
            # If the leftMax is less than the rightMax we want to look at the left side and increment thr pointer and calculate the amount of water on that square. 
            if leftMax < rightMax:
                l+=1 
                # If the height on the current square is the greatest from the left side we want to update leftMax 
                leftMax = max(leftMax, height[l])
                # If leftMax is greater than the current height we can take away the height on the current square to get the amount of water on this square. We don't need to know what the height of the right side is because we know the 'limiting factor' is the left side because leftMax < rightMax, if the current square is the current leftMax this adds 0, so this chain of logic always works
                res += leftMax - height[l]
            else: 
                # If the right side is less than the left we can follow the same logic as the left except decrement closer to the beginning of the list since we are on the right side. 
                r-=1
                rightMax = max(rightMax, height[r])
                res+= rightMax - height[r]
        # By the end we will have the res all added up
        return res 