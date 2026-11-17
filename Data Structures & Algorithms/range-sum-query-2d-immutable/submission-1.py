class NumMatrix:
# IDEA: We can use a 2D prefix sum matrix. Each value assumes it is the bottom right of the matrix, so it is taking in the sum of all elements above it and to the left of it.Then to get O(1) sumRegion we can simply look for where the bottom right is and take the value in that square and subtract what is on the left side for the furthest left column (col1, row2), and the rows above (row1, col2), But we would have actualy over subtracted the top left element at (row1, col1) we actually need to add the top left element onto our result. Since accessing an element in an array is an O(1) operation, we can get the sum in O(1)
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.sumMat = [[0]*(COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1]=prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1-1][col2]
        left = self.sumMat[row2][col1-1]
        topLeft = self.sumMat[row1-1][col1-1]
        return bottomRight - above - left + topLeft 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)