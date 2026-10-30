class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Search through the matrix until we find a 1, which then we perform a BFS on all adjacent cells turning them into -1 to mark them as visited. We keep track of how many times BFS was called at the first level. If we encounter a 0 we skip it.
        ROW = len(grid)
        COL = len(grid[0])
        
        def bfs(r,c):
            # If index is out of bounds, the value is 0 or -1, if it is -1 we have already bfs'd it so we want to avoid double work, and can return early. If it is 0 we want to stop the "spread" and exit the BFS loop. 
            if (r >= ROW or
                c >= COL or
                r < 0 or
                c < 0 or 
                grid[r][c] == '0' or
                grid[r][c] == '-1'):
                return 
            grid[r][c] = '-1'
            bfs(r+1, c)
            bfs(r-1, c)
            bfs(r, c+1)
            bfs(r, c-1)
        
        islands = 0 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    bfs(r,c)
                    islands += 1
        return islands 
