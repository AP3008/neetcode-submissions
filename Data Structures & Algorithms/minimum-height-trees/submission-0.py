class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # undirected so when making adj, has to be bidirectional 
        # Find height of tree and return the min 
        # Idk man this solution is super slow and hard to follow
        adj = { x : set() for x in range(n)}
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        seen = set()
        def bfs(i):
            q = deque([i]) 
            seen = set()
            res = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node in seen: continue
                    seen.add(node)
                    for j in adj[node]:
                        if j in seen: continue 
                        q.append(j)
                res+=1 
            return res 
        res = []
        for i in range(n):
            res.append([bfs(i), i])
        res.sort()

        while res:
            if res[0][0] != res[-1][0]: 
                res.pop()
            else: break 
        return [i for _, i in res]
        
        
            
