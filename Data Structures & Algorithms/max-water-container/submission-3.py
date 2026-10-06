class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = (j-i) * min(heights[i], heights[j])
        maxArea = float('-inf')
        # l, r = 0, len(heights)-1
        # brute force solution 
        #for i in range(len(heights)):
         #   for j in range(i, len(heights)):
          #      area = (j-i)*min(heights[i],heights[j])
           #     if maxArea < area:
            #        maxArea = area
        # return maxArea
        l, r = 0, len(heights)-1
        res = 0
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            if res < area:
                res = area
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return res 

        