class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # We want to look at every index and perform DFS until a treasure chest has been found. THIS IS A O((M*N)^2) sol. and very naive 

        # Actual solution, start from the gates (0) and simultainuosly perform BFS on the gate and marking the distance as the amount of BFS performed from the gate. Some gates may be closer so we need to compare distances at certain indexes for the min. 

        # initialize rows and columns as bounds for the array 
        rows, cols = len(grid), len(grid[0])
        # create a set of indexes that are visited, we store as tuples 
        visit = set()
        # This is our queue, as we need to preserve the order in BFS so we can increment distance properly. 
        q = deque()

        # Helper function to maintain complicated if statement, and avoid repeated work 
        def addIsland(r,c):
            # If the indexes of r or c is out of bound, or the value is a water cell we do not need to add it to our set so we ignore it and return early  
            if (r < 0 or
                r==rows or 
                c < 0 or
                c == cols or
                (r,c) in visit or
                grid[r][c] < 0):
                return 
            # If it makes it here we want to add it to our set of visited indexes, and add it to the back of the queue. 
            visit.add((r,c))
            q.append([r,c])

    # iterate through the matrix
        for r in range(rows):
            for c in range(cols):
                # If we find the treasure we want to start our BFS from there 
                if grid[r][c] == 0:
                    # Because we perform BFS on everything in the queue FIFO, we need to add all treasures first and then BFS on all of them.
                    q.append([r,c])
                    # add to the visited set because we don't want to add treasures back into the queue
                    visit.add((r,c))
        # Starting at distance 0 because we are currently at the treasure and expanding out. 
        dist = 0 
        # We loop while there are elements in the queue, which is the case only when there are still indexes to be explored. 
        while q:
            # We now use a for loop because we need to know that we have explored all of the surrounding tiles before we increment the distance. This for loop gaurentees that the distance being added is accurate, 
            for i in range(len(q)):
                # We are taking the first element of the queue to perform BFS 
                r, c = q.popleft()
                # we can update the current tile to the distance away from treasure, starting at 0 and incrementing the further we explore
                grid[r][c] = dist
                # adding the indexes to the queue if the conditions for doing so are met. 
                addIsland(r+1,c)
                addIsland(r-1, c)
                addIsland(r,c+1)
                addIsland(r,c-1)
        # We increment the distance up by one after we finish a "round" of BFS searches, and have added the next set of indexes to explore, this works because we are using BFS. 
            dist += 1
