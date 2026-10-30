class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #IDEA: Same as other island problem. Perform BFS when we find a '1' then flip it to '-1' to show that it has been explored and for each successful switch we increment the area by 1. We keep track of the max by declaring it above and outside the BFS function. Then on each run we compare the max to the current island count. We take in 3 arguments for BFS row, col, area just so we can use it on the BFS 

        ROW, COL = len(grid), len(grid[0])
        maxArea = 0 
        def bfs(r,c):
            if (r >= ROW or
                c >= COL or 
                r < 0 or 
                c < 0 or 
                grid[r][c] == 0 or
                grid[r][c] == -1):
                return 0
            grid[r][c] = -1
            return 1 + bfs(r+1, c) + bfs(r-1, c) + bfs(r, c+1) + bfs(r, c-1)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea 