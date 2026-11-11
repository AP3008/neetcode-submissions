class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # When we reach the edge we go down if doing row traversal, then that row becomes our new vertical edge so we traverse down to our bottom edge, then iterate backwards through the row, to the left bound the up to the upper bound, and finally right to the right bound. This keeps on following until all of the bounds converge so once the upper bound meets the lower bound and the left bound meets the right bound. 
        RIGHT_BOUND = len(matrix[0])
        LEFT_BOUND = 0
        UP_BOUND = 0
        LOW_BOUND = len(matrix)
    
        res = [] 
        while LEFT_BOUND < RIGHT_BOUND and UP_BOUND < LOW_BOUND:
            # go left to right getting every variable 
            for i in range(LEFT_BOUND, RIGHT_BOUND):
                res.append(matrix[UP_BOUND][i])
            UP_BOUND+=1 
            for i in range(UP_BOUND, LOW_BOUND):
                res.append(matrix[i][RIGHT_BOUND-1])
            RIGHT_BOUND-=1
    
            if not (LEFT_BOUND < RIGHT_BOUND and UP_BOUND < LOW_BOUND):
                break 
            
            for i in range(RIGHT_BOUND-1, LEFT_BOUND-1, -1):
                res.append(matrix[LOW_BOUND-1][i])
            LOW_BOUND-=1 
            for i in range(LOW_BOUND-1, UP_BOUND-1, -1):
                res.append(matrix[i][LEFT_BOUND])
            LEFT_BOUND+=1 
        return res 
    
        


 