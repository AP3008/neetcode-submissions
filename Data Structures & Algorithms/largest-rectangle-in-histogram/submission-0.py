class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This uses a stack so there is some relation of popping taht we can use to get an O(n) solution. 
        # Area = height * width => min(height) * max(width)
        # The minimum area will always be min(heights) * len(heights)

        # Our tracker of the max area we've seen
        maxArea = 0
        stack = [] # we append paris (index, height)

        for i, h in enumerate(heights):
            # this is our current index so when we pop elements we know from where we can start from when caluclatiung the max area. 
            start = i 
            # If the current height is greater than the element at the end of the stack we need to pop it off and calculate the max height we could have gotten from it's index to the current index as the width, and the height as the height 
            while stack and stack[-1][-1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            # If we popped elements of the stack, we can use their index as our starting index because they are larger than the current values height, so we can take use part of their block.
            stack.append((start,h))
        for i, h in stack:
            # These are the elements that made it to the end of the array, so we can subtract the length of the array to their start index to caluclate the maxArea achievable for the remaining elements in the stack 
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea 


