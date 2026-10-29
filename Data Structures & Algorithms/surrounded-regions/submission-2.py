class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # We look around the outside of the board looking for O's 
        # if there is an O we want to perform a DFS on it looking for the O's that connect to it. All O's in this DFS get turned into a T's. Once the entire perimeter is scanned we loop through the entire array turning the T's into O's 

        # MY SOL. AFTER HEARING NEETCODE EXPLAIN THE SOLUTION 
        ROW, COL = len(board), len(board[0])

        def dfs(r,c):
            if (r >= ROW or
                c >= COL or 
                r < 0 or 
                c < 0 or 
                board[r][c] == 'X' or 
                board[r][c] == 'T'): 
                return 
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROW):
            if board[r][COL-1] == 'O':
                dfs(r, COL-1)
            if board[r][0] == 'O':
                dfs(r,0)
        
        for c in range(COL):
            if board[ROW-1][c]:
                dfs(ROW-1, c)
            if board[0][c]:
                dfs(0, c)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'