class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # We want to look at every index and perform DFS until a treasure chest has been found. THIS IS A O((M*N)^2) sol. and very naive 

        # Actual solution, start from the gates (0) and simultainuosly perform BFS on the gate and marking the distance as the amount of BFS performed from the gate. Some gates may be closer so we need to compare distances at certain indexes for the min. 

        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if (r < 0 or
                r==rows or 
                c < 0 or
                c == cols or
                (r,c) in visit or
                grid[r][c] < 0):
                return 
            visit.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r+1,c)
                addRoom(r-1, c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1
