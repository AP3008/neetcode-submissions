class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
       # My Sol. Create adjacency list and perform DFS on each node. Have a set that keeps track of the seen nodes and increment the components count by 1 every time we find a node that isn't apart of the seen set. 

       # Also cover edge cases, if n = 0 
        if not n:
            return 0 
        # create adj. list 
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # set to track what has been seen
        seen = set()
        components = 0 
        def dfs(node):
            if node in seen:
                return False
            seen.add(node)
            for j in adj[node]:
                dfs(j)
            return True 
        for v in adj:
            if dfs(v) == False:
                continue 
            components+=1 
        return components


            
