class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 
        # taking the rows and cols length of heights 
        ROWS, COLS = len(heights), len(heights[0])

        # making a set of indexes that can reach the pacific and atlantic ocean respectively 
        pac, atl = set(), set()

        # Depth first search on a specific index 
            # Takes the args: 
                # r,c: which are the index
                # visit: the set that we want to append the index with if it can reach said ocean set
                # prevHeight: we are looking for greater heights so we want to keep track of the previous heights, the reason we are looking for greater heights is because we are working from the edges that 100% can reach the ocean inside. If the height at that index is greater then we can conclude we need to add them to the set. 
        def dfs(r,c, visit, prevHeight):
            # If any of these conditions are met we do not add them to the set:
                # the index is already inside of the set 
                # if the index ranges are out of bounds for the graph 
                # if the current height is less than the previous height, if it is less than the previous height we can conclude that, that direction is not valid for it.
            if ((r,c) in visit or
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                    return 
            # If it passes these conditions we can add it to the respective ocean set, as it can make it to that ocean. 
            visit.add((r,c))
            # Then we explore all of the neighbours of that index, using the current index for the previous height to see if this direction is valid. If going inwards we find greater heights that outside we can say it is a valid way to reach the ocean. 
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        # We know that all of the edges of the matrix will be able to reach at least one ocean, so we want to perform our DFS on all of the indexes that are on the edges of the matrix. 

        # We will first start by all of the ones on the Top (Pacific) and Bottom (Atlantic) and we use the heights at the edge as the previous height for the iwards dfs search. The second dfs is the bottom one which is closer to the atlantic. 
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c,atl, heights[ROWS-1][c])

        # The exact same process but now for the left (pacific) and right (Atlantic) edges 
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        # We now want to create our res set 
        res = []
        # We loop through the matrix and check if the index are in both teh pacific and atlantic set, if so we can append the element to res, if not we don't add it. 
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res 