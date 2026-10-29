class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # We look around the outside of the board looking for O's 
        # if there is an O we want to perform a DFS on it looking for the O's that connect to it. All O's in this DFS get turned into a T's. Once the entire perimeter is scanned we loop through the entire array turning the T's into O's 

        # MY SOL. AFTER HEARING NEETCODE EXPLAIN THE SOLUTION 
        
        #Grabbing the row and cols
        ROW, COL = len(board), len(board[0])

        # A dfs function to explore and to mark all connected 'O's as T's
        def dfs(r,c):
            # If the index is out of range we return,
            # If the value at this index is an 'X' or already turned into a 'T' we want to conclude searching from this index
            if (r >= ROW or
                c >= COL or 
                r < 0 or 
                c < 0 or 
                board[r][c] == 'X' or 
                board[r][c] == 'T'): 
                return 

            # If it makes it past the checks it must be a 'O' that is connected to the edge of the board or another 'O' that is. Then we turn it into a 'T' so we know that it should remain an 'O' on the last iteration. 
            board[r][c] = 'T'
            # we perform a DFS on all indexes vertical and horizontal to it. 
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

    # We loop through the edge of the board starting with the top and bottom 
        for r in range(ROW):
            # If we spot an 'O' on either the top or bottom we need to dfs on it.  
            if board[r][COL-1] == 'O':
                dfs(r, COL-1)
            if board[r][0] == 'O':
                dfs(r,0)

        # We loop through the perimeter Left and Right this time
        for c in range(COL):
            # if we find an 'O' on the left or right we need to perform a DFS on that index 
            if board[ROW-1][c]:
                dfs(ROW-1, c)
            if board[0][c]:
                dfs(0, c)

    # We loop through the entire board marking everything as an 'X' except for 'T' which get turned into an 'O'
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

            # Since the changes were in-place we don't return anything. 