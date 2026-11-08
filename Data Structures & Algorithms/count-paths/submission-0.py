class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We can only move right or down, so that means that every block can be accessed from the left of it or the top. So squares with no left and no top have no way to be accessed, but every square can be accessed from either. The only squares that have one way of being accessed are the squares on the boarder. We use a DP 2D array to store the how many ways to access a specific element. The number of ways will always be the square below it plus the square on the right. We keep on recursively solving that until we get to the end of the board. 

        # We have our row which is all we will need to compute as we build it in reverse order. 
        row = [1] * n 

        # We loop through the rows creating a corresponding row for each row that we visit 
        for i in range(m-1):
            # Since we know what the row will include on the first iteration (all 1's), we can use that as the current row that we are calculating.
            newRow = [1] * n
            # We loop from n-2 because the edge of the matrix will have 1, so we can start from the element to the right of it, and work backwards through the row, since the closer we get to the beginning the more ways we will have to reach there. 
            for j in range(n-2,-1,-1):
                # The newRow[j] will be the sum of the element to it's right and the element directly under it, which will be row[j]
                newRow[j] = newRow[j+1]+row[j]
            # We make the newRow we calculated the old row, so we can use it in the following calculations
            row = newRow
        # At the end, the element in the first index of the row will be the sum of all possible ways to reach the beginning from the end. 
        return row[0]

