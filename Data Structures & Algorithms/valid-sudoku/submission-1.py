class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Have a hashset that checks each row and col 
        # To have a hashset for each block (3x3) space, we can represent indicies with taking the floor division 3 of the column and floor division 3 of the row, and using that as the key for the hashmap that stores the hashset 

        colDict = defaultdict(set)
        rowDict = defaultdict(set)
        blockDict = defaultdict(set)
        ROW = COL = 9 

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] != ".":
                    if board[r][c] in colDict[c] or board[r][c] in rowDict[r] or board[r][c] in blockDict[(r//3,c//3)]:
                        return False 
                    colDict[c].add(board[r][c])
                    rowDict[r].add(board[r][c])
                    blockDict[(r//3,c//3)].add(board[r][c])
        return True 

                