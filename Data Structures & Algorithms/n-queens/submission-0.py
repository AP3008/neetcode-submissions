class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # THOUGHTS: So now two queens can be on the same row or col. The diaganals logic becomes hard, so if a queen is in (r,c) we cant have queens in (r+1,c+1), ... , (r+(n-r), c+(n-c)). If we were to check that, it would be a lot of brute force algorithims so there has to be another way that is simpler than placing the queen and corss checking each square that it doens't invalidate some queen. We can check the columns easily because for negative diagonals row-col along the neg. diag. will equal the same thing and for the positive diagonal we use row + col to get the number. If any of these have been seen we skip over that slot. 
    
        col = set() # set to track columns seen 
        posDiag = set() # (r+c) tracking the positive diagonals
        negDiag = set() # (r-c) tracking negative diagonals 
    
        res = [] # resulting list 
        # creating an nxn board with "." in every position
        board = [["."] * n for i in range(n)]
    
        # Our backtrack function which takes in the row that we are on. 
        def backtrack(r):
            # If the row is equal to n we have iterated through the entire board and found a solution
            if r == n:
                # We take a copy of the current board state and add it to our res 
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            # For each column in the board we want to iterate, in the current function call this will be only for the current row. 
            for c in range(n):
                # If the column has been seen, or we are on a taken pos. diag. or neg. diag. we want to continue. We don't have to check the row, because we only increment on valid previous solutions, so the row doens't have to be checked.
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue 
                # If we are on a valid spot for a queen we add the column to our col hashset 
                col.add(c)
                # We add the diagonal combination that has been taken in this iteration. 
                posDiag.add(r+c)
                negDiag.add(r-c)
                # We add a Queen to the current psoition 
                board[r][c] = "Q"

                # Then we continue using this board state and explore further to see if a valid solution can come out of this board state.
                backtrack(r+1)

                # This is our backtracking, we remove the element from each of the sets and reverse all the affects of the board state from this iteration, so previous iterations can use the previous board state. This gets popped all the way back to the original call, as each decision comes back with an output when r reached n. 
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        # We want to start our backtrack at row 0, and return the res from this. 
        backtrack(0)
        return res 
    