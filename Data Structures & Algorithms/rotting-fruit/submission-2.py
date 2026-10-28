class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       # Find rotten fruit, perform BFS turning all visited indexes rotten, and we keep track of the amount of BFS searches it takes to turn fruit rotten. If there are fruit that are not rotten we return False

        row, col = len(grid), len(grid[0])

       # Create deque 
        q = deque()

       # idea: have a set that tracks regular fruit, and make sure it is empty at the end of the queue, set.pop() as fruits are visited and turned rotten. 
        fruits = set() 

        def bfs(r,c):
            # Check if the index is a fruit and if so we add it to the q 
            if (r >= row or
                c >= col or
                c < 0 or
                r < 0):
                # If any of these conditions are met, we don't add to the q
                return
            if grid[r][c] == 2 or grid[r][c] == 0:
                return  
            grid[r][c] = 2
            fruits.remove((r,c))
            q.append([r,c])

        # minutes starts at 0 
        minutes = 0
        # BRAINSTORM NOT IMPLEMENTED: So we keep track of the number of empty cells, because row * col = area of grid, iff area - no. rotten fruits (len(q)) == emptyCtr we can return back 0 as all of the fruits are rotten, but this misses some edge cases so don't implement    

        # We need to find all rotten fruit and add it to the queue 
        # Then need to check that all elements aren't already rotten 

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    # We put a tuple because lists are unhashable
                    fruits.add((r,c))
        if len(fruits) == 0:
            return 0 
        # Go through the q while it is full of rotten fruits
        while q: 
            # We want to explore every fruit in this BFS rotation before we increment the clock
            for i in range(len(q)):
            # Taking the rotten fruits to BFS
                r,c = q.popleft()
                # Exploring surrounding tiles of the rotten fruit
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            # After this rotation is done we want to increment the minutes as in this next minute all explored fruits have turned rotten  
            minutes+=1
            if len(fruits) == 0:
                break 
        # We return minutes only if all fruits have become rotten. 
        return minutes if len(fruits) == 0 else -1 
                

        